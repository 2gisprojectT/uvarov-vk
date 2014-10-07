__author__ = 'admin'

from unittest import TestCase
from Numbers import Numbers
import unittest


class NumbersTest(TestCase):
    def test_init(self):
        num = Numbers(1, 2, 3)
        self.assertEqual(1, num.a, 'A is wrong')
        self.assertEqual(2, num.b, 'B is wrong')
        self.assertEqual(3, num.c, 'C is wrong')

    def test_multiplication(self):
        num = Numbers(1, -2, 3)
        self.assertEqual(-6, num.multiplication(), 'Mult is wrong')

    def test_abs_multiplication(self):
        num = Numbers(1, -2, 3)
        self.assertEqual(6, num.abs_multiplication(), 'Abs Mult is wrong')


if __name__ == '__main__':
    unittest.main()
