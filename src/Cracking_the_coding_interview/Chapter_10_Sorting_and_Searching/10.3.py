def search_rotated_array(arr, target, low=0, high=None):
    """
    Modified binary search.
    cut the array in two
    Time: O(log n) <- binary search
    Space: O(log n ) <- stack frames
    """
    if high is None:
        high = len(arr) - 1

    ## implement base case len(arr) == 0 or 1
    if high - low < 2:
        if arr[low] == target:
            return low
        if arr[high] == target:
            return high
        return None

    pivot = low + (high - low)//2

    # Normal cases
    if arr[low] <= target <= arr[pivot]:
        return search_rotated_array(arr, target, low, pivot)
    elif arr[pivot] <= target <= arr[high]:
        return search_rotated_array(arr, target, pivot, high)

    # the wrap around is in the interval
    # pivot is right of the wraparound but the pattern pivot < target < high wasn't seen: target must be in lower half
    elif arr[pivot] <= arr[high] <= arr[low]:
        return search_rotated_array(arr, target, low, pivot)
    # pivot is left of wraparound but the pattern low < target < pivot wasn't seen: target must be in upper half
    elif arr[high] <= arr[low] <= arr[pivot]:
        return search_rotated_array(arr, target, pivot, high)


arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print(search_rotated_array(arr, 5))

