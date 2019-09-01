def find_nearest_left(arr, index):
    while arr[index] == '':
        index -= 1
    return index


def sparse_search(arr: list, target: str, low=0, high=None):
    """
    modified binary search where you need logic to handle hitting empty string.
    Time: log(n), n is number of non sparse values, but due to find nearest_left, algorithm is O(n)
    Space: log(n), number of stack frames
    """
    if high is None:
        high = find_nearest_left(arr, len(arr) - 1)

    pivot = find_nearest_left(arr, low + (high-low)//2)
    if arr[pivot] == target:
        return pivot
    elif arr[low] == target:
        return low
    elif arr[high] == target:
        return high
    elif arr[pivot] < target:
        return sparse_search(arr, target, pivot, high)
    else:
        return sparse_search(arr, target, low, pivot)


arr = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
print(sparse_search(arr, 'dad'))
