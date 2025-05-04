
# # Target Count Divisible by K

# Given a sorted array of integers, `arr`, a target value, `target`, and a positive integer, `k`, return whether the number of occurrences of the target in the array is a multiple of `k`.

# ```
# Example 1: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 2, k = 3
# Output: True. 2 occurs 6 times, which is a multiple of 3.

# Example 2: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 2, k = 4
# Output: False. 2 occurs 6 times, which is not a multiple of 4.

# Example 3: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 4, k = 3
# Output: True. 4 occurs 0 times, and 0 is a multiple of any number.
# ```

# Constraints:

# - 1 ≤ arr.length ≤ 10^5
# - -10^9 ≤ arr[i], target ≤ 10^9
# - 1 ≤ k ≤ 10^5
# - arr is sorted in ascending order

# Approach:
# Find the target, then spread out in either direction to find the no. of occurrences
# T: O(logn + n) = O(n)
# S: O(1) extra space

# Better approach:
# Find the first occurrence of the target, and the last occurrence.
# Subtract the latter index from the former, and then I have the occurrence count 
# T: O(logn + logn + 1) = O(logn)


# [1, 2, 2, 2, 2, 2, 2, 3]   # 2
#  l
#                    
#     h      
def first_occurrence(arr: list, target: int):
    low, high = 0,  len(arr) - 1 

    while (high - low) > 1:
        mid = (high + low) // 2
        if arr[mid] < target: # before target
            low = mid
        else:
            high = mid
    if arr[high] == target:
        return high
    return -1 

# [1, 2, 2, 2, 2, 2, 2, 3]   # 2
#                    l
#                    
#                       h

def last_occurrence(arr: list, target: int):
    low, high = 0,  len(arr) - 1 

    while (high - low) > 1:
        mid = (high + low) // 2
        if arr[mid] <= target:   # before or equal to target
            low = mid
        else:
            high = mid
    if arr[low] == target:
        return low
    return -1 

# Example 3: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 4, k = 3
# ([1, 2, 2, 2, 2, 2, 2, 3], 2, 4)}")
def occurrences_multiple_of_k(arr: list, target: int, k: int):
    # edge case handling 
    # empty array
    if not arr or len(arr) == 0:
        return True # zero occurrences
    # one element
    if len(arr) == 1:
        return True
    # if the target is bigger than the largest element or smaller than the smallest 
    if arr[len(arr) - 1] < target or arr[0] > target:
        return True         # zero occurrences again 

    index_of_first_occurrence = first_occurrence(arr, target)
    print(index_of_first_occurrence)

    index_of_last_occurrence = last_occurrence(arr, target)
    print(index_of_last_occurrence)

    occurrences = index_of_last_occurrence - index_of_first_occurrence + 1
    if occurrences % k == 0: # multitple of k
        # handle 0 occurrences
        return True
    return False

import unittest

class Tests(unittest.TestCase):
    def test_handles_question_example(self):
        self.assertEqual(occurrences_multiple_of_k(
            [1, 2, 2, 2, 2, 2, 2, 3], 2, 4), False)

    def test_handles_empty_list(self):
        self.assertEqual(occurrences_multiple_of_k(
            [], 2, 4), True)

unittest.main(exit=False)


# print(f"target={2} k={4} res={occurrences_multiple_of_k([1, 2, 2, 2, 2, 2, 2, 3], 2, 4)}")
