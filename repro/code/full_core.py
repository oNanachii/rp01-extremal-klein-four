"""Fixed-polar eight-dimensional census: binary truth tables and exact matrices.

No prior-round code is imported.  Every one of 2^16 linear refinements is
tested through shifts of three directly computed Walsh tables.  Character
sums, raw dual phases (including constants), and the polar-isometry orbit
are checked separately from the parameter proof.
"""
from collections import Counter, deque
from itertools import product
import json
from pathlib import Path


def mul(x, y):
    z = 0
    while y:
        if y & 1:
            z ^= x
        y >>= 1
        x <<= 1
        if x & 4:
            x ^= 7
    return z


def tr(x):
    return x ^ mul(x, x)


def coords(v):
    return tuple((v >> (2 * i)) & 3 for i in range(4))


def encode(t):
    return sum(x << (2 * i) for i, x in enumerate(t))


def base(v):
    a, b, c, d = coords(v)
    return mul(a, d) ^ mul(b, c) ^ tr(mul(a, c))


def fwht(values):
    values = list(values)
    step = 1
    while step < len(values):
        for start in range(0, len(values), 2 * step):
            for i in range(start, start + step):
                x, y = values[i], values[i + step]
                values[i], values[i + step] = x + y, x - y
        step *= 2
    return values


def parity(x):
    return x.bit_count() & 1


base_values = [base(v) for v in range(256)]
scalar_base = [[tr(mul(z, q)) for q in base_values] for z in (1, 2, 3)]
walsh = [fwht([1 - 2 * q for q in row]) for row in scalar_base]
assert all(set(abs(x) for x in row) == {16} for row in walsh)
phase = [[sum((walsh[j][x ^ shift] < 0) << x for x in range(256))
          for shift in range(256)] for j in range(3)]
all_bits = (1 << 256) - 1
summary = Counter()
equality = set()
maximum_count = 0
for l1 in range(256):
    for l2 in range(256):
        signs = (walsh[0][l1], walsh[1][l2], walsh[2][l1 ^ l2])
        if signs == (16, 16, 16):
            maximum_count += 1
            dbits = phase[0][l1] ^ phase[1][l2] ^ phase[2][l1 ^ l2]
            gauss = 256 - 2 * dbits.bit_count()
            summary[gauss] += 1
            if gauss == -64:
                equality.add((l1, l2))

# In binary Fourier coordinates, a pair of coefficient bits is represented
# by the unique rho such that dot(bits,a)=Tr(rho*a).
dual = {tr(z) | (tr(mul(z, 2)) << 1): z for z in range(4)}
fourier = [tuple(dual[x] for x in coords(v)) for v in range(256)]
predicted_nonconstant = {}
for f, ell, h, i in product(range(4), repeat=4):
    word = 0
    for index, (rho, sigma, tau, upsilon) in enumerate(fourier):
        value = tr(mul(sigma, upsilon) ^ mul(f ^ h, upsilon)
                   ^ mul(ell ^ i, sigma) ^ mul(i, rho) ^ mul(h, tau))
        word |= value << index
    predicted_nonconstant[f, ell, h, i] = word


def binary_linear_masks(coefficients):
    # Tuple is (f,g,ell,m,h,k,i,j); the input order is a,b,c,d.
    f, g, ell, m, h, k, i, j = coefficients
    images = []
    for linear, frobenius in ((f, g), (h, k), (ell, m), (i, j)):
        images.extend((linear ^ frobenius,
                       mul(linear, 2) ^ mul(frobenius, 3)))
    return tuple(sum(tr(mul(z, image)) << i for i, image in enumerate(images))
                 for z in (1, 2))


parameter_equality = set()
raw_phase_checked = 0
branch_signs = Counter()
linear_bijection = set()
equal_sign_equations_checked = 0
for parameters in product(range(4), repeat=8):
    f, g, ell, m, h, k, i, j = parameters
    l1, l2 = binary_linear_masks(parameters)
    linear_bijection.add((l1, l2))
    dbits = phase[0][l1] ^ phase[1][l2] ^ phase[2][l1 ^ l2]
    constant = dbits & 1
    gamma = tr(mul(i, mul(k, k)) ^ mul(h, mul(j, j)) ^ mul(j, k)
               ^ mul(g, j) ^ mul(m, k))
    assert constant == gamma, parameters
    expected = predicted_nonconstant[f, ell, h, i] ^ (all_bits if constant else 0)
    assert dbits == expected, parameters
    raw_phase_checked += 1
    if h == i == 0 and tr(mul(f, ell)) == 1:
        pattern = ''.join('+' if val > 0 else '-' for val in
                          (walsh[0][l1], walsh[1][l2], walsh[2][l1 ^ l2]))
        branch_signs[pattern] += 1
    if h == i == 0:
        actual_signs = (walsh[0][l1], walsh[1][l2], walsh[2][l1 ^ l2])
        same_sign = len(set(actual_signs)) == 1
        first_equation = (mul(f, mul(j, j)) ^ mul(ell, mul(k, k))) == mul(j, k)
        assert same_sign == first_equation
        if same_sign:
            assert (actual_signs[0] < 0) == tr(mul(g, j) ^ mul(m, k) ^ mul(j, k))
        equal_sign_equations_checked += 1
    if h == i == j == k == 0 and tr(mul(f, ell)) == 1:
        parameter_equality.add((l1, l2))

assert len(linear_bijection) == 65536
assert parameter_equality == equality
assert len(equality) == 96
assert branch_signs['---'] == 0 and branch_signs['+++'] == 96


def linear_apply(columns, v):
    out = 0
    for i, column in enumerate(columns):
        if (v >> i) & 1:
            out ^= column
    return out


def shear(direction, c0, c1, v):
    a, b, c, d = coords(v)
    if direction == 0:
        a, b = a ^ mul(c0, c), b ^ mul(c0, d) ^ mul(c1, c)
    else:
        c, d = c ^ mul(c0, a), d ^ mul(c0, b) ^ mul(c1, a)
    return encode((a, b, c, d))


generators = [tuple(shear(direction, c0, c1, 1 << i) for i in range(8))
              for direction in (0, 1) for c0, c1 in ((1, 0), (2, 0), (0, 1), (0, 2))]
for columns in generators:
    assert len({linear_apply(columns, v) for v in range(256)}) == 256
    for x in range(8):
        for y in range(8):
            old = base((1 << x) ^ (1 << y)) ^ base(1 << x) ^ base(1 << y)
            new = base(columns[x] ^ columns[y]) ^ base(columns[x]) ^ base(columns[y])
            assert old == new


def pullback(point, columns):
    return tuple(sum((scalar_base[component][column] ^ parity(point[component] & column)) << j
                     for j, column in enumerate(columns)) for component in range(2))


representative = binary_linear_masks((1, 0, 2, 0, 0, 0, 0, 0))
orbit = {representative}
queue = deque(orbit)
while queue:
    point = queue.popleft()
    for columns in generators:
        image = pullback(point, columns)
        assert image in equality
        if image not in orbit:
            orbit.add(image)
            queue.append(image)
assert orbit == equality

identity = tuple(1 << i for i in range(8))
matrix_group = {identity}
queue = deque(matrix_group)
while queue:
    current = queue.popleft()
    for generator in generators:
        following = tuple(linear_apply(current, column) for column in generator)
        if following not in matrix_group:
            matrix_group.add(following)
            queue.append(following)
assert len(matrix_group) == 3840

# Independent direct 4-variable truth tables for EVERY refinement of one
# semisimple plane, before assuming it is K-homogeneous.
semisimple_phase_checks = 0
for F, G, L, M in product(range(4), repeat=4):
    values = [mul(v & 3, v >> 2) ^ mul(F, v & 3)
              ^ mul(G, mul(v & 3, v & 3)) ^ mul(L, v >> 2)
              ^ mul(M, mul(v >> 2, v >> 2)) for v in range(16)]
    spectra = [fwht([1 - 2 * tr(mul(z, q)) for q in values]) for z in (1, 2, 3)]
    assert all(abs(s) == 4 for row in spectra for s in row)
    for frequency in range(16):
        rho, sigma = dual[frequency & 3], dual[frequency >> 2]
        actual = sum(row[frequency] < 0 for row in spectra) & 1
        predicted = tr(mul(L, rho) ^ mul(F, sigma) ^ mul(G, M))
        assert actual == predicted
        semisimple_phase_checks += 1

result = {
    'method': 'Independent F2 truth tables, fast Walsh transform, translated sign bitsets, binary input matrices; no prior-round imports',
    'core_refinements_checked': len(linear_bijection),
    'raw_dual_phase_identities_including_constant_checked': raw_phase_checked,
    'core_equal_sign_equivalence_checked': equal_sign_equations_checked,
    'semisimple_raw_phase_checks_before_homogeneity_assumption': semisimple_phase_checks,
    'maximum_self_inverse_refinements': maximum_count,
    'dual_gauss_distribution_in_maximum_branch': dict(sorted(summary.items())),
    'negative_end_parameter_subset_equals_walsh_subset': parameter_equality == equality,
    'necessary_trace_one_branch_sign_patterns': dict(sorted(branch_signs.items())),
    'negative_end_orbit_size': len(orbit),
    'binary_generated_isometry_group_order': len(matrix_group),
    'isometry_stabilizer_order': len(matrix_group) // len(orbit),
    'mathematical_scope': 'Numerical checks of the eight-dimensional core only; general even-n classification requires the analytic decomposition and compensation arguments.'
}
print(json.dumps(result, ensure_ascii=False, indent=2))
