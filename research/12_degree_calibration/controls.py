#!/usr/bin/env python3
"""Exact arithmetic diagnostics; these do not certify the IUT bridge.

Only integers and Fraction are used. Logarithms are represented by their
rational coefficients relative to one formal log(p), never approximated.
"""

from fractions import Fraction as F
from itertools import product
from math import prod


def rational_prime_factors(value):
    """Return the nonzero valuations of a nonzero rational number."""
    value = abs(F(value))
    assert value
    factors = {}
    for number, sign in ((value.numerator, 1), (value.denominator, -1)):
        divisor = 2
        while divisor * divisor <= number:
            while number % divisor == 0:
                factors[divisor] = factors.get(divisor, 0) + sign
                number //= divisor
            divisor += 1
        if number > 1:
            factors[number] = factors.get(number, 0) + sign
    return {p: n for p, n in factors.items() if n}


def arithmetic_control():
    for p in (2, 3, 5, 101):
        q = {'p': F(1, p), 'infinity': F(1)}
        h = {'p': F(1, p * p), 'infinity': F(1)}
        local_norms = {'p': F(1, p), 'infinity': F(1)}
        image = {v: q[v] * local_norms[v] for v in q}
        assert image == h
        assert prod(q.values()) > prod(h.values())
        assert prod(local_norms.values()) == F(1, p)
        # Delta=-log(p), S=0, b-a=-log(p).
        assert F(-2) - F(-1) == F(-1) + F(0)
        global_norms = {'p': F(1, p), 'infinity': F(p)}
        assert prod(global_norms.values()) == 1
        assert q['infinity'] * global_norms['infinity'] > h['infinity']
    for value in (F(12, 5), F(1, 6), F(11), F(-7, 15)):
        finite_norm = prod(F(p) ** (-n)
                           for p, n in rational_prime_factors(value).items())
        assert finite_norm * abs(value) == 1
    return 8


def local_model_control():
    cases = 0
    for a, b in product(range(-4, 5), repeat=2):
        # Ideals pi^a O -> pi^b O have model coordinates -a,-b.
        alpha, beta = -a, -b
        k = b - a
        z = a + k - b
        assert z == 0 and alpha + z == beta + k
        assert a + k == b
        # The inverse uses -k. A fixed coefficient 1 is integral iff a>=b.
        assert b - k == a
        assert (a - b >= 0) == (alpha <= beta)
        cases += 1
    assert -1 != -2 + 0  # The fixed identity coefficient fails for Q_p,H_p.
    assert -1 == -2 + 1  # The free coefficient p gives an isomorphism.
    for q_radius, h_radius in ((F(1), F(1, 3)), (F(2, 5), F(7, 2))):
        t = h_radius / q_radius
        assert t * q_radius == h_radius
        assert (h_radius / (t * q_radius)) == 1  # zero archimedean divisor
        cases += 1
    return cases


def composition_control():
    cases = 0
    for n, m, e, f, z, w in product((1, 2), (1, 3), (1, 2),
                                   (1, 3), (0, 2), (0, 5)):
        alpha, beta, gamma = F(-2), F(1, 2), F(3)
        u = n * alpha + z - e * beta
        v = m * beta + w - f * gamma
        composite_z = e * w + m * z
        composite_u = e * v + m * u
        assert composite_z >= 0
        assert m * n * alpha + composite_z == e * f * gamma + composite_u
        cases += 1
    return cases


def packet_normalization_control():
    cases = 0
    # Numerical realizations of the dimension identity in (G5), not IUT data.
    for mod_degrees, extension_degrees in (((1, 3), (2, 1)),
                                           ((1, 2), (2, 1))):
        d = sum(mod_degrees)
        for n in range(1, 5):
            total = F(0)
            for indices in product(range(len(mod_degrees)), repeat=n):
                n_tau = prod(extension_degrees[i] for i in indices)
                dimension = prod(mod_degrees[i] * extension_degrees[i]
                                 for i in indices)
                total += F(dimension, n_tau * d ** n)
                if mod_degrees == (1, 2):
                    # Every K_v is complex; C^(tensor_R n) has 2^(n-1) factors.
                    assert dimension == 2 * 2 ** (n - 1)
            assert total == 1
            cases += 1
    assert sum(F(1, 3) for _ in range(3)) == 1  # procession average
    return cases


def weighted_accounting_control():
    weights = (F(1, 2), F(1, 3), F(1, 6))
    q = (F(-1), F(-2), F(0))
    h = (F(-3), F(-1), F(2))
    defect = (F(-3), F(0), F(1))
    image = tuple(x + t for x, t in zip(q, defect))
    slack = tuple(y - x for x, y in zip(image, h))
    assert all(s >= 0 for s in slack)
    weighted = lambda xs: sum(w * x for w, x in zip(weights, xs))
    a, b = weighted(q), weighted(h)
    delta, s = weighted(defect), weighted(slack)
    assert b - a == delta + s
    # Structural reference is subtracted, and the SAME M is used on both sides.
    reference = (F(2), F(-1), F(3, 2))
    for m in (6, 12, 30):
        corrected_q = tuple(m * (x + o) - m * o for x, o in zip(q, reference))
        corrected_h = tuple(m * (x + o) - m * o for x, o in zip(h, reference))
        assert weighted(corrected_q) / m == a
        assert weighted(corrected_h) / m == b
        assert (weighted(corrected_h) - weighted(corrected_q)) / m == delta + s
    # The prescribed root and positive exponent are retained algebraically.
    ell, tate_order, m = 5, F(3), 10
    root_order = tate_order / (2 * ell)
    assert m * root_order == 3 and (-m * root_order) / m == -root_order
    return 5


def ordered_picard_control():
    a = F(-7, 3)
    for c in (F(1, 2), F(1), F(2)):
        delta = (c - 1) * a
        assert (delta >= 0) == (c <= 1)
        assert (delta == 0) == (c == 1)
    # A negative pilot fixes scale only when its numerical image is also fixed.
    assert F(2) * a < 0 and F(2) * a != a
    return 3


if __name__ == '__main__':
    controls = (arithmetic_control, local_model_control, composition_control,
                packet_normalization_control, weighted_accounting_control,
                ordered_picard_control)
    total = 0
    for control in controls:
        count = control()
        total += count
        print(f'PASS: {control.__name__} ({count} exact cases)')
    print(f'PASS: {total} exact cases across {len(controls)} controls; no floating point.')
    print('LIMIT: diagnostics and accounting checks do not certify Gamma_chi or the IUT bridge.')
