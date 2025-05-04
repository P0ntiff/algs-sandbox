def merge(nums, start, mid, end, helper):
    for i in range(start, end + 1):
        helper[i] = nums[i]

    i, j = start, mid + 1
    fill = i
    while i <= mid and j <= end:
        if helper[i] <= helper[j]:
            nums[fill] = helper[i]
            i += 1
        else:
            nums[fill] = helper[j]
            j += 1
        fill += 1
    while i <= mid:
        nums[fill] = helper[i]
        i += 1
        fill += 1
    # no need to copy remaining elements from the right sub array, they are already in place

# [1, 2, 5, 4, 3] len = 5
# start = 0, end = 4, mid = 2
# [1, 2, 5] [4, 3]

# [1, 2, 5]
# start = 0, mid = 1, end = 2
# [1, 2] [5]

# [1, 2, 5]
# start = 0, mid = 1 end = 1

def merge_sort_helper(nums, start, end, helper):
    if start >= end:
        return 
    mid = (start + end) // 2
    # merge left then right
    merge_sort_helper(nums, start, mid, helper)
    merge_sort_helper(nums, mid + 1, end, helper)

    # merge two halves
    merge(nums, start, mid, end, helper)

def merge_sort(nums):
    """
    Sorts a list of numbers in ascending order using the merge sort algorithm.

    Args:
        nums: A list of numbers to be sorted.

    Returns:
        A new list containing the sorted numbers.
    """
    if not nums:
        return []
    merge_sort_helper(nums, 0, len(nums) - 1, [0 for _ in range(len(nums))])
    return nums 


# [1 , 2, 5, 4, 3] len = 5


import unittest

class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_order(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(merge_sort([5, 2, 8, 1, 9, 2, 4]), [1, 2, 2, 4, 5, 8, 9])

if __name__ == '__main__':
    unittest.main()