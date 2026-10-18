"""Exact CMP2018 equation (4) / F16 coordinate substitution.

This checks four chosen core maps, not all refinements or group types.
K = F2[alpha]/(alpha^2+alpha+1), represented by 0,1,2,3.
L = K[beta]/(beta^2+beta+alpha), represented by x0 + beta*x1.
"""

from itertools import product
from pathlib import Path
import json


def kmul(x, y):
    out = 0
    for _ in range(2):
        if y & 1:
            out ^= x
        y >>= 1
        x <<= 1
        if x & 4:
            x ^= 7
    return out


def ksq(x):
    return kmul(x, x)


def ktrace(x):
    return x ^ ksq(x)


def lmul(x, y):
    a, b = x & 3, x >> 2
    c, d = y & 3, y >> 2
    lo = kmul(a, c) ^ kmul(2, kmul(b, d))
    hi = kmul(a, d) ^ kmul(b, c) ^ kmul(b, d)
    return lo | (hi << 2)


def ltrace(x):
    # Tr_L/K(x0+beta*x1)=x1; beta^4=beta+1.
    return ktrace(x >> 2)


def h_value(a, c, co):
    f, g, ell, m, eta, k, theta, j = co
    return (ktrace(kmul(a, c)) ^ kmul(f, a) ^ kmul(g, ksq(a))
            ^ kmul(ell, c) ^ kmul(m, ksq(c)))


def q_value(v, co):
    a, b, c, d = v
    f, g, ell, m, eta, k, theta, j = co
    return (kmul(a, d) ^ kmul(b, c) ^ h_value(a, c, co)
            ^ kmul(eta, b) ^ kmul(k, ksq(b))
            ^ kmul(theta, d) ^ kmul(j, ksq(d)))


def mm_parameters(z, co):
    f, g, ell, m, eta, k, theta, j = co
    lo = kmul(z, theta) ^ kmul(ksq(z), ksq(j))
    hi = kmul(z, eta) ^ kmul(ksq(z), ksq(k))
    return lo | (hi << 2)


def mm_g(z, y, co):
    return lmul(z, lmul(4, h_value(y & 3, y >> 2, co)))


def cmp_phase(z, xi, co):
    rho, sigma, tau, upsilon = xi
    u = upsilon | (sigma << 2)
    vv = (tau ^ rho) | (rho << 2)
    yy = lmul(ksq(z), u ^ mm_parameters(z, co))
    return ltrace(lmul(vv, yy) ^ mm_g(z, yy, co))


def pairing(v, xi):
    out = 0
    for x, y in zip(v, xi):
        out ^= kmul(x, y)
    return ktrace(out)


def run():
    assert lmul(4, 4) ^ 4 == 2
    assert all(any(lmul(a, b) == 1 for b in range(1, 16))
               for a in range(1, 16))
    vectors = list(product(range(4), repeat=4))
    covectors = vectors
    pairing_table = [[pairing(v, xi) for v in vectors] for xi in covectors]
    cases = {
        "base_core": (0, 0, 0, 0, 0, 0, 0, 0),
        "Q_star": (1, 0, 2, 0, 0, 0, 0, 0),
        "negative_core_from_example_7_1": (0, 2, 0, 0, 0, 0, 0, 1),
        "generic_refinement": (2, 3, 1, 2, 1, 2, 3, 1),
    }
    evidence = {"scope": "4 specified core maps; no orbit enumeration",
                "field": "beta^2+beta=alpha over F4", "cases": {}}
    for name, co in cases.items():
        for v in vectors:
            a, b, c, d = v
            x, y = (b ^ d) | (d << 2), a | (c << 2)
            for z in (1, 2, 3):
                pi_y = lmul(z, y) ^ mm_parameters(z, co)
                actual = ktrace(kmul(z, q_value(v, co)))
                lifted = ltrace(lmul(x, pi_y) ^ mm_g(z, y, co))
                assert actual == lifted, (name, v, z, "input")
        truth = {z: [ktrace(kmul(z, q_value(v, co))) for v in vectors]
                 for z in (1, 2, 3)}
        for xi, pairing_row in zip(covectors, pairing_table):
            for z in (1, 2, 3):
                walsh = sum(1 - 2 * (q ^ pairing_bit)
                            for q, pairing_bit in zip(truth[z], pairing_row))
                assert walsh == 16 * (-1) ** cmp_phase(z, xi, co), (
                    name, xi, z, "Walsh")
        origin = [16 * (-1) ** cmp_phase(z, (0, 0, 0, 0), co)
                  for z in (1, 2, 3)]
        gd = sum((-1) ** (cmp_phase(1, xi, co)
                          ^ cmp_phase(2, xi, co)
                          ^ cmp_phase(3, xi, co)) for xi in vectors)
        evidence["cases"][name] = {
            "coefficients_f_g_ell_m_eta_k_theta_j": co,
            "input_identity_checks": 256 * 3,
            "direct_Walsh_checks": len(covectors) * 3,
            "original_Gauss_sums": origin,
            "actual_dual_sum_character_sum": gd,
            "v4_if_on_maximum_s_branch": 4627 + 4 * gd
            if origin == [16, 16, 16] else None,
        }
    assert evidence["cases"]["Q_star"]["actual_dual_sum_character_sum"] == -64
    assert evidence["cases"]["base_core"]["actual_dual_sum_character_sum"] == 64
    return evidence
