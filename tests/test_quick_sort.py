import unittest

from algorithms.quick_sort import quick_sort


class QuickSortTest(unittest.TestCase):

    def test_quick_sort_should_return_empty_list_for_empty_list(self):
        self.assertEqual(quick_sort([]), [])

    def test_quick_sort_should_return_same_list_for_single_element_list(self):
        self.assertEqual(quick_sort([1]), [1])

    def test_quick_sort_should_sort_list_correctly(self):
        self.assertEqual(quick_sort([5, 2, 3, 9, 1]), [1, 2, 3, 5, 9])

    def test_quick_sort_with_duplicate_values(self):
        self.assertEqual(
            quick_sort([2, 5, 6, 1, 1, 5, 8, 3, 1]),
            [1, 1, 1, 2, 3, 5, 5, 6, 8]
        )

    def test_quick_sort_for_whole_duplicate_list(self):
        self.assertEqual(
            quick_sort([1, 1, 1, 1, 1]),
            [1, 1, 1, 1, 1]
        )

    def test_quick_sort_with_negative_positive_values(self):
        self.assertEqual(
            quick_sort([9, -2, 0, 5, 12, 3, -1]),
            [-2, -1, 0, 3, 5, 9, 12]
        )
