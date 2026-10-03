#!/usr/bin/env python3
"""Finite controls of the audit method, not IUT models or a p-adic implementation.

Run: python3 research/09_log_step_adequacy/diagnostic_controls.py
Control C's source interpretation is a written argument in SOURCE_CONTRACT.md;
its tests here check only exact arithmetic and the coverage distinction.
"""
from fractions import Fraction as F
import unittest


def compose(first, second):
    """second after first, with equality of the actual intermediate witness."""
    return {(x, z) for x, y in first for middle, z in second if y == middle}


def image(relation, left, right):
    return {(left(x), right(y)) for x, y in relation}


def chart_witness(input_mass, chart_mass):
    """Coefficient of chi_log(S), using the supplied mu(log(S))=mu(S)."""
    if input_mass < 0 or chart_mass <= 0:
        raise ValueError('Nonnegative mass and an ample chart are required')
    coefficient = input_mass / chart_mass
    return coefficient, coefficient * chart_mass


class AdequacyControls(unittest.TestCase):
    def test_A_identity_on_marked_quotient(self):
        records = {('Q0', 'a0'), ('Q0', 'a1'), ('Q1', 'a0')}
        diagonal = {(x, x) for x in records}
        quotient = lambda x: (x[0], 'same-volume')
        actual = image(diagonal, quotient, quotient)
        values = {quotient(x) for x in records}
        self.assertEqual(actual, {(x, x) for x in values})
        self.assertNotIn((('Q0', 'same-volume'), ('Q1', 'same-volume')), actual)

    def test_B_separate_quotients_create_spurious_composition(self):
        first = {('x', 'y0')}
        second = {('y1', 'z')}
        identity = lambda x: x
        middle_q = lambda _: 'Y'
        self.assertEqual(compose(first, second), set())
        qfirst = image(first, identity, middle_q)
        qsecond = image(second, middle_q, identity)
        self.assertEqual(compose(qfirst, qsecond), {('x', 'z')})
        self.assertEqual(image(compose(first, second), identity, identity), set())

    def test_B_retaining_the_middle_witness_blocks_the_false_path(self):
        first = {('x', ('Y', 'y0', 'Q0'))}
        second = {(('Y', 'y1', 'Q0'), 'z')}
        self.assertEqual(compose(first, second), set())
        genuinely_matching = {(('Y', 'y0', 'Q0'), 'z')}
        self.assertEqual(compose(first, genuinely_matching), {('x', 'z')})

    def test_B_native_tags_cannot_be_rechosen(self):
        first = {('x', ('Q0', F(1, 9)))}
        second = {(('Q1', F(1, 9)), 'z')}
        self.assertEqual(compose(first, second), set())

    def test_C_rss_chart_calculation_is_exact(self):
        for mass in [F(0), F(1, 81), F(1, 9), F(1), F(7, 3)]:
            for chart_mass in [F(1, 27), F(1, 81)]:
                coefficient, output_mass = chart_witness(mass, chart_mass)
                self.assertGreaterEqual(coefficient, 0)
                self.assertEqual(output_mass, mass)

    def test_C_native_power_and_normalization_bookkeeping(self):
        # Symbolic Haar masses for nu(q O)=-2 log(3); not sampled IUT input.
        p, order, power = 3, 2, 4
        for r in range(4):
            mass = F(1, p ** (order * power * r))
            _, output_mass = chart_witness(mass, F(1, 27))
            self.assertEqual(output_mass, mass)
            degree_in_log_p_units = -F(order * power * r)
            self.assertEqual(degree_in_log_p_units / power, -F(order * r))

    def test_C_numeric_composition_uses_a_valid_middle_representative(self):
        mass = F(1, 9)
        _, intermediate_mass = chart_witness(mass, F(1, 27))
        _, final_mass = chart_witness(intermediate_mass, F(1, 81))
        self.assertEqual(final_mass, mass)
        # This works because this numerical operation accepts every Fn mass.
        # No analogous totality is assumed for admissible IPL histories.

    def test_C_equal_volume_is_not_a_membership_proof(self):
        marked_native_mass = F(1, 9)
        _, represented_mass = chart_witness(marked_native_mass, F(1, 27))
        separately_restricted_family = {F(1, 81)}
        self.assertEqual(represented_mass, marked_native_mass)
        self.assertNotIn(represented_mass, separately_restricted_family)
        # A logical separation only; this family is NOT an IUT abstraction.

    def test_invalid_chart_domain_is_rejected(self):
        for mass, chart in [(F(-1), F(1)), (F(1), F(0)), (F(1), F(-1))]:
            with self.assertRaises(ValueError):
                chart_witness(mass, chart)


if __name__ == '__main__':
    unittest.main(verbosity=2)
