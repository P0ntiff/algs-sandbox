

def is_before(arr: list, index: int, target: int):
    return arr[index] < target 

def binary_search(arr: list, target: int):
    if len(arr) == 0:
        return -1
    low, high = 0, len(arr) -1
    if arr[low] >= target or arr[high] < target:
        if arr[low] == target:
            return 0
        return -1
    while high - low > 1:
        mid = (low + high) // 2
        if (is_before(arr, mid, target)):
            low = mid
        else:
            high = mid
    if arr[high] == target:
        return high 
    return -1

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