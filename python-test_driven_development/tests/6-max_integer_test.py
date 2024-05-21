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


if __name__ == "__main__":
    unittest.main()
