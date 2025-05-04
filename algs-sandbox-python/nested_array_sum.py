
# Given a nested array, arr, return its sum
def nested_array_sum(arr):
    res = 0
    for element in arr:
        if isinstance(element, int):
            res += element
        else:
            res += nested_array_sum(element)
    return res

#arr = [1, [2, 3], [4, [5]], 6]
# output = 21






def nested_array_sum(arr):
    """Approach: recursively parse array with a helper that takes an index.
       Add the sum and return it
       Base Case: A number, and end of the array
       Recursive Case: Not a number, needs to be called on
    """
    output = 0
    for elem in arr:
        if isinstance(elem, int):
            output += elem
        else:
            output += nested_array_sum(elem)
    return output


print(nested_array_sum([1, [2, 3], [4, [5]], 6]))