import unittest
from algorithms.selection_sort import selection_sort


class SelectionSortTest(unittest.TestCase):

    def test_selection_sort_accepts_argument_and_return_result(self):
        self.assertEqual(selection_sort(1), None)

    def test_selection_sort_accepts_argument_of_type_list_only(self):
        self.assertIsNone(selection_sort("Text"), "Should return None if the param is not of type list")
        self.assertIsInstance(selection_sort([1, 2, 3]), list)
        self.assertEqual(selection_sort([1, 2, 3]), [1, 2, 3])

    def test_selection_sort_must_have_one_element_at_least(self):
        self.assertEqual(selection_sort([]), None)

    def test_selection_sort_sorts_unsorted_list(self):
        self.assertEqual(selection_sort([0]), [0])
        self.assertEqual(selection_sort([5, 7, 3, 2]), [2, 3, 5, 7])
        self.assertEqual(selection_sort([10, 2, 7, 8, 9, 1]), [1, 2, 7, 8, 9, 10])
        self.assertEqual(selection_sort([8, 7, 6, 5, 4, 3, 2, 1, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(selection_sort([0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0])
        self.assertEqual(selection_sort([1, 1, 2, 1, 1]), [1, 1, 1, 1, 2])
        self.assertEqual(selection_sort(["C", "B", "A", "Z", "W", "F"]), ["A", "B", "C", "F", "W", "Z"])
        self.assertEqual(selection_sort([True, False, False, True, 2, 1]), [False, False, True, True, 1, 2])
