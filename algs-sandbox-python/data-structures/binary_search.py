def binary_search(nums, target):
    """
    Performs a binary search on a sorted list of integers.

    Args:
        nums: A sorted list of integers.
        target: The integer to search for.

    Returns:
        The index of the target if found in the list, otherwise -1.
    """
    low = 0
    high = len(nums) - 1
    while low <= high: 
        mid = (low + high) // 2           # integer division
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1  # search lower half
        else:
            low = mid + 1 # search upper half
    return -1   # not found

import unittest

class TestBinarySearch(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([5], 5), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([5], 3), -1)

    def test_multiple_elements_found_first(self):
        self.assertEqual(binary_search([2, 4, 6, 8, 10], 2), 0)

    def test_multiple_elements_found_middle(self):
        self.assertEqual(binary_search([2, 4, 6, 8, 10], 6), 2)

    def test_multiple_elements_found_last(self):
        self.assertEqual(binary_search([2, 4, 6, 8, 10], 10), 4)

    def test_multiple_elements_not_found_smaller(self):
        self.assertEqual(binary_search([2, 4, 6, 8, 10], 1), -1)

    def test_multiple_elements_not_found_larger(self):
        self.assertEqual(binary_search([2, 4, 6, 8, 10], 12), -1)

    def test_multiple_elements_not_found_between(self):
        self.assertEqual(binary_search([2, 4, 6, 8, 10], 5), -1)

if __name__ == '__main__':
    unittest.main()