import unittest
from algorithms.recursion import sum_using_recursion


class RecursionTest(unittest.TestCase):

    def test_sum_using_recursion_return_zero_if_empty_array_passed(self):
        self.assertEqual(sum_using_recursion([]), 0)

    def test_sum_using_recursion_return_list_element_if_single_value_list_passed(self):
        self.assertEqual(sum_using_recursion([3]), 3)

    def test_sum_using_recursion_return_sum_of_list(self):
        self.assertEqual(sum_using_recursion([1, 2, 3, 4]), 10)
