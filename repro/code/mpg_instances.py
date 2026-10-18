"""Version-specific MPG13 examples: explicit Boolean polynomials and F4 arithmetic.

The four-dimensional example uses Boolean ANFs only. The project-compatible
eight-dimensional example is checked both by Boolean ANFs and by F4 arithmetic.
The proof of inequivalence is the unequal common-zero count, not a failed search.
"""
from itertools import product
import json
from pathlib import Path


def mul(u, v):
    """F4 = F2[alpha]/(alpha^2+alpha+1), alpha represented by 2."""
    p = 0
    for i in range(2):
        if (v >> i) & 1:
            p ^= u << i
    if p & 4:
        p ^= 7
    return p


def tr(u):
    ans = u ^ mul(u, u)
    assert ans in (0, 1)
    return ans


def small(v, A, B):
    a, b, c, d = [(v >> i) & 1 for i in range(4)]
    q = (a & d) ^ (b & c)
    return q, q ^ (a & c) ^ (A & a) ^ (B & c)


def rank(rows, n):
    rows = list(rows)
    ans = 0
    for j in range(n):
        piv = next((i for i in range(ans, len(rows)) if rows[i] & (1 << j)), None)
        if piv is None:
            continue
        rows[ans], rows[piv] = rows[piv], rows[ans]
        for i in range(len(rows)):
            if i != ans and (rows[i] & (1 << j)):
                rows[i] ^= rows[ans]
        ans += 1
    return ans


def polar_ranks(q, n):
    result = []
    for mask in (1, 2, 3):
        scalar = lambda x: sum(q(x)[i] for i in range(2) if mask & (1 << i)) % 2
        rows = [sum((scalar((1 << i) ^ (1 << j)) ^ scalar(1 << i)
                     ^ scalar(1 << j)) << j for j in range(n)) for i in range(n)]
        result.append(rank(rows, n))
    return result


def invariants(q, n):
    vals = [q(v) for v in range(1 << n)]
    zeros = [v for v, value in enumerate(vals) if value == (0, 0)]
    pairs = sum(vals[u ^ v] == (0, 0) for u in zeros if u for v in zeros if v and v != u)
    assert pairs % 6 == 0
    return {
        "polar_ranks": polar_ranks(q, n),
        "common_zeros": len(zeros),
        "zero_F2_planes": pairs // 6,
        "Gauss_sums": [sum((-1) ** (sum(value[i] for i in range(2)
                               if mask & (1 << i)) % 2) for value in vals)
                       for mask in (1, 2, 3)],
    }


def eight_anf(v, target):
    a0, a1, b0, b1, c0, c1, d0, d1 = [(v >> i) & 1 for i in range(8)]
    qinf = (a0*d0 + a0*d1 + a1*d0 + b0*c0 + b0*c1 + b1*c0) % 2
    qzero = (a0*d0 + a1*d1 + b0*c0 + b1*c1 + a0*c0 + a0*c1 + a1*c0) % 2
    if target != "zero":
        qzero ^= a0
    if target == "trace_one":
        qzero ^= c0 ^ c1
    return qinf, qzero


def eight_field(v, A, B):
    a, b, c, d = [(v >> (2*i)) & 3 for i in range(4)]
    cross = mul(a, d) ^ mul(b, c)
    return tr(mul(2, cross)), tr(mul(3, cross) ^ mul(2, mul(a, c))
                                  ^ mul(mul(2, A), mul(a, a))
                                  ^ mul(mul(2, B), mul(c, c)))


def project_input(v):
    """Q_{f,g,l,m}, f=alpha^2,g=alpha,l=m=1; then (c,d)->alpha(c,d)."""
    a, b, c, d = [(v >> (2*i)) & 3 for i in range(4)]
    c, d = mul(2, c), mul(2, d)
    Q = mul(a, d) ^ mul(b, c) ^ tr(mul(a, c))
    Q ^= mul(3, a) ^ mul(2, mul(a, a)) ^ c ^ mul(c, c)
    return tr(Q), tr(mul(2, Q))


def run():
    # S(a,b,c,d)=(a,b+c,c,d+a+c) swaps the two small input forms.
    for v in range(16):
        a, b, c, d = [(v >> i) & 1 for i in range(4)]
        sv = a | ((b ^ c) << 1) | (c << 2) | ((d ^ a ^ c) << 3)
        assert small(sv, 1, 1) == small(v, 1, 1)[::-1]
    small_results = {f"A={A},B={B}": invariants(lambda v: small(v, A, B), 4)
                     for A, B in [(1, 1), (1, 0), (0, 0)]}
    assert [x["common_zeros"] for x in small_results.values()] == [4, 8, 8]
    assert all(x["polar_ranks"][:2] == [4, 4] for x in small_results.values())

    cases = [("trace_one", 1, 2), ("H", 1, 0), ("zero", 0, 0)]
    eight_results = {}
    for name, A, B in cases:
        for v in range(256):
            assert eight_anf(v, name) == eight_field(v, A, B)
            if name == "trace_one":
                assert eight_anf(v, name) == project_input(v)
        out = invariants(lambda v: eight_anf(v, name), 8)
        out["Tr_AB"] = tr(mul(A, B))
        eight_results[name] = out
    assert [x["zero_F2_planes"] for x in eight_results.values()] == [245, 277, 277]
    assert all(x["polar_ranks"] == [8, 8, 8] for x in eight_results.values())
    assert all(x["common_zeros"] == 76 for x in eight_results.values())

    # Independently test the residual SL2(F4) formula (only 60 matrices).
    matrices = [s for s in product(range(4), repeat=4) if mul(s[0], s[3]) ^ mul(s[1], s[2]) == 1]
    assert len(matrices) == 60
    for A, B in product(range(4), repeat=2):
        for p, q, r, s in matrices:
            Ap = mul(A, mul(p,p)) ^ mul(p,r) ^ mul(B, mul(r,r))
            Bp = mul(A, mul(q,q)) ^ mul(q,s) ^ mul(B, mul(s,s))
            assert tr(mul(Ap, Bp)) == tr(mul(A, B))

    return {"scope": "explicit examples and residual formula only; no GL(8,2) or group enumeration",
            "four_dimensional": small_results, "swap_identity_checked_at": 16,
            "eight_dimensional": eight_results,
            "ANF_vs_F4_checks": 3*256, "project_parameter_instance_checks": 256,
            "SL2_F4_formula_checks": 16*60}

