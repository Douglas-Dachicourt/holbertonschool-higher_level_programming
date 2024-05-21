#!/usr/bin/python3
import unittest
"""Unittest for max_integer([..])
"""
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        expected_list = None
        self.assertEqual(max_integer([]), expected_list)

    def test_few_numbers(self):
        expected_list = 8
        self.assertEqual(max_integer([-1, 2, -10, 8]), expected_list)

    def test_string_inside(self):
        expected_list = "you"
        self.assertEqual(max_integer(["hello", "you"]), expected_list)

    def test_max_beggining(self):
        expected_list = 100
        self.assertEqual(max_integer([100, 98, 2, -10, 99]), expected_list)

    def test_max_middle(self):
        expected_list = 65
        self.assertEqual(max_integer([10, 8, 65, -10, 45]), expected_list)

    def test_one_element(self):
        expected_list = 20
        self.assertEqual(max_integer([20]), expected_list)


if __name__ == "__main__":
    unittest.main()
