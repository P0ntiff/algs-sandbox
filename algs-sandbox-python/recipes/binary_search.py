


def is_before(arr: list, index: int, target):
    return arr[index] < target


def find_transition_point(arr: list, target: int):
    low = 0
    high = len(arr)

    while (high - low) > 1:
        mid = (high + low) // 2
        if (is_before(arr, mid, taret)):
            low = mid
        else: 
            high = mid
    return high # the last element before, or the first element after, or something else


