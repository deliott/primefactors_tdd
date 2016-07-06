"""
primefactorstests.py
:created on: 20160706
__author__ = 'Eliott Dupont'
:License: GPL3
"""


import unittest
from primefactorstdd.primefactors import factors_of


class TestPrimeFactors(unittest.TestCase):
    """test suite for PrimeFactors"""

    def test_factors_of_1(self):
        """tests if factors_of(1) returns []"""
        self.assertEqual(factors_of(1), [])

    def test_factors_of_2(self):
        """tests if factors_of(2) returns [2]"""
        self.assertEqual(factors_of(2), [2])

    def test_factors_of_3(self):
        """tests if factors_of(3) returns [3]"""
        self.assertEqual(factors_of(3), [3])

    def test_factors_of_4(self):
        """tests if factors_of(4) returns [2]"""
        self.assertEqual(factors_of(4), [2, 2])

    def test_factors_of_5(self):
        """tests if factors_of(5) returns [5]"""
        self.assertEqual(factors_of(5), [5])

    def test_factors_of_6(self):
        """tests if factors_of(6) returns [2,3]"""
        for elt in factors_of(6):
            self.assertIn(elt, [2, 3])

    def test_factors_of_7(self):
        """tests if factors_of(7) returns [7]"""
        self.assertEqual(factors_of(7), [7])

    def test_factors_of_8(self):
        """tests if factors_of(8) returns [2, 2, 2]"""
        self.assertEqual(factors_of(8), [2, 2, 2])


if __name__ == '__main__':
    unittest.main()