#!/usr/bin/env python3
"""Bounded, exact checks accompanying RP01; Python standard library only.

The light mode reconstructs every selected map as a binary ANF, counts its
zero planes directly, and compares that count with the Walsh-moment identity.
The full mode additionally checks all 2^16 refinements of ONE fixed polar.
Neither mode establishes the general decomposition or equality classification.
"""

import argparse
from datetime import datetime, timezone
from itertools import combinations, product
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

from cmp_mm import run as check_cmp
from mpg_instances import run as check_mpg


class Field:
    def __init__(self, degree, modulus):
        self.degree, self.modulus, self.size = degree, modulus, 1 << degree

    def mul(self, x, y):
        out = 0
        while y:
            if y & 1:
                out ^= x
            y >>= 1
            x <<= 1
            if x & self.size:
                x ^= self.modulus
        return out

    def trace(self, x):
        out, term = 0, x
        for _ in range(self.degree):
            out ^= term
            term = self.mul(term, term)
        assert out in (0, 1)
        return out


K, L = Field(2, 0b111), Field(3, 0b1011)


def parity(v):
    return v.bit_count() & 1


def coords(v, widths):
    out = []
    for width in widths:
        out.append(v & ((1 << width) - 1))
        v >>= width
    assert v == 0
    return out


def q4(v, affine=False):
    u, w = coords(v, [2, 2])
    return K.mul(u, w) ^ (u if affine else 0)


def q6(v, negative=False):
    x, y = coords(v, [3, 3])
    xy = L.mul(x, y)
    second = L.mul(2, xy) ^ (x ^ L.mul(7, y) if negative else 0)
    return L.trace(xy) | (L.trace(second) << 1)


def q8(v, compensation=False):
    a, b, c, d = coords(v, [2, 2, 2, 2])
    out = K.mul(a, d) ^ K.mul(b, c) ^ K.trace(K.mul(a, c))
    if compensation:
        return out ^ K.mul(2, K.mul(a, a)) ^ K.mul(d, d)
    return out ^ a ^ K.mul(2, c)


def minus(v):
    u, w = coords(v, [2, 2])
    return K.mul(u, w) ^ K.mul(u, u) ^ K.mul(2, K.mul(w, w))


def odd10(v):
    # The F8 map already uses the manuscript's binary target coordinates.
    plane = q4(v >> 6)
    target = K.trace(plane) | (K.trace(K.mul(2, plane)) << 1)
    return q6(v & 63, True) ^ target


def even12(v, compensation=False):
    return q8(v & 255, compensation) ^ (minus(v >> 8) if compensation else q4(v >> 8))


def teaching_nilpotent8(v):
    # Explainer 4.6: polynomial basis (1,t,t^2,t^3), t^4=t^2+1.
    x, y = v & 15, v >> 4
    multiplication_by_t = (8, 1, 10, 4)
    uy = sum(parity(row & y) << i for i, row in enumerate(multiplication_by_t))
    q1 = parity(x & y)
    q2 = parity(x & uy) ^ parity(7 & x) ^ parity(13 & y)
    return q1 | (q2 << 1)


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            bit = row.bit_length() - 1
            if bit in pivots:
                row ^= pivots[bit]
            else:
                pivots[bit] = row
                break
    return len(pivots)


def inverse(rows):
    n = len(rows)
    a = [row | (1 << (n + i)) for i, row in enumerate(rows)]
    for i in range(n):
        j = next(j for j in range(i, n) if a[j] >> i & 1)
        a[i], a[j] = a[j], a[i]
        for j in range(n):
            if j != i and a[j] >> i & 1:
                a[j] ^= a[i]
    return [row >> n for row in a]


def compose(a, b):
    return [xor_items(b[j] for j in range(len(b)) if row >> j & 1) for row in a]


def xor_items(items):
    out = 0
    for item in items:
        out ^= item
    return out


def minpoly(matrix):
    n = len(matrix)
    power = [1 << i for i in range(n)]
    pivots = {}
    for degree in range(n + 1):
        value = sum(row << (n * i) for i, row in enumerate(power))
        relation = 1 << degree
        while value:
            bit = value.bit_length() - 1
            if bit not in pivots:
                pivots[bit] = value, relation
                break
            old_value, old_relation = pivots[bit]
            value ^= old_value
            relation ^= old_relation
        else:
            return relation
        power = compose(power, matrix)
    raise AssertionError("No Cayley-Hamilton dependence")


def remainder(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def squarefree(poly):
    derivative = sum(((poly >> j) & 1) << (j - 1) for j in range(1, poly.bit_length(), 2))
    a, b = poly, derivative
    while b:
        a, b = b, remainder(a, b)
    return a == 1


def fwht(values):
    out = list(values)
    step = 1
    while step < len(out):
        for start in range(0, len(out), 2 * step):
            for i in range(start, start + step):
                x, y = out[i], out[i + step]
                out[i], out[i + step] = x + y, x - y
        step *= 2
    return out


def stats(name, dimension, definition, expected_v4=None, actual_subgroups=False):
    """Reconstruct binary ANF, then use it independently of field evaluation."""
    size, h = 1 << dimension, 1 << (dimension // 2)
    assert definition(0) == 0
    linear = [definition(1 << i) for i in range(dimension)]
    cross = {(i, j): definition((1 << i) ^ (1 << j)) ^ linear[i] ^ linear[j]
             for i, j in combinations(range(dimension), 2)}
    values = []
    for v in range(size):
        support = [i for i in range(dimension) if v >> i & 1]
        reconstructed = xor_items(linear[i] for i in support)
        reconstructed ^= xor_items(cross[i, j] for i, j in combinations(support, 2))
        assert reconstructed == definition(v)
        values.append(reconstructed)
    polars, spectra = [], []
    for char in (1, 2, 3):
        polars.append([sum(parity(char & cross[min(i, j), max(i, j)]) << j
                           for j in range(dimension) if j != i)
                       for i in range(dimension)])
        spectra.append(fwht([1 - 2 * parity(char & q) for q in values]))
    assert all(rank(b) == dimension for b in polars)
    assert all(abs(x) == h for row in spectra for x in row)
    inv = [inverse(b) for b in polars]
    c = [inv[0][i] ^ inv[1][i] ^ inv[2][i] for i in range(dimension)]
    zeros = [i for i, q in enumerate(values) if q == 0]
    zero_set = set(zeros)
    t0 = sum((x ^ y) in zero_set for x in zeros for y in zeros)
    # An F2 plane has 3 nonzero vectors and 3 unordered generating pairs.
    pair_count = sum((x ^ y) in zero_set for x, y in combinations(zeros[1:], 2))
    assert pair_count % 3 == 0
    planes = pair_count // 3
    assert t0 == 3 * len(zeros) - 2 + 6 * planes
    s, j2 = 4 * len(zeros), 16 * t0
    v4 = 16 * planes + 6 * len(zeros) - 5
    assert j2 == 3 * s - 2 + 6 * v4
    moment = sum(a * b * c for a, b, c in zip(*spectra))
    gauss = [row[0] for row in spectra]
    if gauss == [h, h, h]:
        mn = (h**4 + 9*h**3 + 36*h*h - 36*h + 8) // 24
        assert v4 == mn + moment // (4 * size)
    if expected_v4 is not None:
        assert v4 == expected_v4
    result = dict(name=name, dimension_V=dimension, half_dimension_n=dimension // 2,
                  group_order=4*size, original_Gauss_sums=gauss,
                  polar_ranks=[rank(b) for b in polars], dual_polar_rank=rank(c),
                  zero_vectors=len(zeros), s=s, T0=t0, J2=j2,
                  zero_binary_planes=planes, v4=v4, triple_Walsh_moment=moment,
                  raw_dual_character_sum=moment // h**3,
                  truth_table_reconstructed_from_binary_ANF=True)
    if dimension in (8, 10) and name in ("Q_star", "odd_lower_n5"):
        changes = []
        for i, j in product(range(3), repeat=2):
            if i == j:
                continue
            poly = minpoly(compose(inv[i], polars[j]))
            changes.append(dict(ordered_character_pair=[i+1, j+1],
                                minimal_polynomial=bin(poly), semisimple=squarefree(poly)))
        assert all(item["semisimple"] == (dimension == 10) for item in changes)
        result["all_six_target_basis_changes"] = changes
    if actual_subgroups:
        def cocycle(x, y):
            out = 0
            for i in range(dimension):
                if x >> i & 1:
                    if y >> i & 1:
                        out ^= linear[i]
                    for j in range(i+1, dimension):
                        if y >> j & 1:
                            out ^= cross[i, j]
            return out
        involutions = [(v, w) for v, w in product(zeros, range(4)) if (v, w) != (0, 0)]
        subgroups = set()
        ordered_commuting_pairs = 2 * len(involutions) + 1
        for (x, u), (y, w) in combinations(involutions, 2):
            f = cocycle(x, y)
            if f == cocycle(y, x):
                third = x ^ y, u ^ w ^ f
                subgroups.add(frozenset(((x, u), (y, w), third)))
                ordered_commuting_pairs += 2
        ordered_commuting_pairs += len(involutions)
        assert len(subgroups) == v4 and ordered_commuting_pairs == j2
        result["actual_Klein_subgroups_in_central_extension"] = len(subgroups)
        result["actual_ordered_commuting_involutory_pairs"] = ordered_commuting_pairs
    return result


def check_normalizers():
    checked = 0
    for f, ell, g, m in product(range(4), repeat=4):
        if K.trace(K.mul(f, ell)) != 1:
            continue
        finv = next(x for x in range(1, 4) if K.mul(f, x) == 1)
        for v in range(256):
            a, b, c, d = coords(v, [2]*4)
            # Pullback M1 M2 M3 M4: apply rightmost input change first.
            if K.mul(f, ell) == 3:
                b ^= K.mul(2, c)  # M4
                a, b = a ^ K.mul(2, c), b ^ K.mul(2, d)  # M3
            a, b, c, d = K.mul(finv, a), K.mul(finv, b), K.mul(f, c), K.mul(f, d)
            b, d = b ^ K.mul(m, c), d ^ K.mul(g, a)  # M1
            q = K.mul(a, d) ^ K.mul(b, c) ^ K.trace(K.mul(a, c))
            q ^= K.mul(f, a) ^ K.mul(g, K.mul(a, a)) ^ K.mul(ell, c) ^ K.mul(m, K.mul(c, c))
            assert q == q8(v)
        checked += 1
    assert checked == 96
    return dict(coordinate_maps=96, vectors_per_map=256,
                target_fixed=True, proof_scope="Explicit substitutions, not a search for equivalences")


def check_double_negative_and_target_lifts():
    columns = [(0, 1, 0, 1), (0, 1, 1, 1), (1, 0, 1, 0), (2, 1, 2, 0)]
    for x in product(range(4), repeat=4):
        sx = [xor_items(K.mul(coefficient, column[j]) for coefficient, column in zip(x, columns))
              for j in range(4)]
        lhs = minus(sx[0] | sx[1] << 2) ^ minus(sx[2] | sx[3] << 2)
        assert lhs == K.mul(x[0], x[1]) ^ K.mul(x[2], x[3])
    for scalar, exponent in product((1, 2, 3), (1, 2)):
        for u, v in product(range(4), repeat=2):
            sigma_u = u if exponent == 1 else K.mul(u, u)
            sigma_v = v if exponent == 1 else K.mul(v, v)
            uv = K.mul(u, v)
            sigma_uv = uv if exponent == 1 else K.mul(uv, uv)
            assert K.mul(K.mul(scalar, sigma_u), sigma_v) == K.mul(scalar, sigma_uv)
    assert rank([sum(((column[j] >> k) & 1) << (2*j+k)
                     for j in range(4) for k in range(2))
                 for column in columns] +
                [sum(((K.mul(2, column[j]) >> k) & 1) << (2*j+k)
                     for j in range(4) for k in range(2)) for column in columns]) == 8
    return dict(negative_pair_to_positive_pair_columns=columns,
                all_256_vectors_checked=True, all_six_target_lifts_checked=True,
                consequence="Q_star plus two negative planes is equivalent to Q_star plus two positive planes")


def light():
    examples = [
        stats("n2_lower", 4, lambda v: q4(v, True), 53, True),
        stats("n2_upper", 4, q4, 69, True),
        stats("n3_lower", 6, lambda v: q6(v, True), 431),
        stats("n3_upper", 6, q6, 463),
        stats("Q_star", 8, q8, 4371),
        stats("teaching_nilpotent_eight", 8, teaching_nilpotent8, 4371),
        stats("odd_lower_n5", 10, odd10, 56443),
        stats("even_lower_n6", 12, even12, 787019),
        stats("compensation_not_lower_n6", 12, lambda v: even12(v, True), 819787),
        stats("negative_core", 8, lambda v: q8(v, True)),
        stats("negative_plane", 4, minus),
    ]
    return dict(selected_examples=examples,
                all_96_explicit_normalizers=check_normalizers(),
                double_negative_remainder=check_double_negative_and_target_lifts(),
                version_specific_MPG_instances=check_mpg(),
                CMP_equation_4_common_F16_substitution=check_cmp())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("light", "full"))
    parser.add_argument("--output", type=Path,
                        help="JSON destination (default: ../results/checks_MODE.json)")
    args = parser.parse_args()
    if not __debug__:
        parser.error("Run without -O: exact checks use Python assertions")
    started = time.perf_counter()
    result = light()
    if args.mode == "full":
        completed = subprocess.run([sys.executable, str(Path(__file__).with_name("full_core.py"))],
                                   check=True, capture_output=True, text=True)
        result["fixed_polar_full_census"] = json.loads(completed.stdout)
    files = sorted(Path(__file__).parent.glob("*.py"))
    record = dict(format_version=1, mode=args.mode, status="passed",
                  executed_utc=datetime.now(timezone.utc).isoformat(),
                  python_version=platform.python_version(),
                  elapsed_seconds=round(time.perf_counter()-started, 6),
                  source_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
                  mathematical_scope="Bounded finite checks; not a proof of the general theorems",
                  results=result)
    dest = args.output or Path(__file__).parent.parent / "results" / f"checks_{args.mode}.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: record[key] for key in ("mode", "status", "python_version", "elapsed_seconds")}, indent=2))


if __name__ == "__main__":
    main()
