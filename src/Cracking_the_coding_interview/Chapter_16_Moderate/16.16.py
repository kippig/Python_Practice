def subsort(arr):
    """
    :param arr:
    :return: m, n such that you can sort the array between just those indices
    """

    def find_prefix(arr):
        i = 0
        while i < len(arr) + 1 and arr[i] < arr[i + 1]:
            i += 1
        return i

    def find_suffix(arr):
        i = len(arr) - 1
        while i >= 1 and arr[i] > arr[i - 1]:
            i -= 1
        return i

    def binary_search(arr, target, lower, upper):
        pivot = (upper + lower)//2
        if abs(upper - lower) <= 1:
            return upper, lower
        elif arr[pivot] > target:
            return binary_search(arr, target, lower, pivot)
        elif arr[pivot] < target:
            return binary_search(arr, target, pivot, upper)

    prefix = find_prefix(arr)
    suffix = find_suffix(arr)
    if prefix == len(arr):
        return None, None

    maximum, minimum = arr[prefix], arr[suffix]

    # Check the middle to see if we need to move more of either the suffix or prefix
    for i in range(prefix + 1, suffix):
        if arr[i] < minimum:
            minimum = arr[i]
        elif arr[i] > maximum:
            maximum = arr[i]

    m = max(*binary_search(arr, minimum, 0, prefix))
    n = min(*binary_search(arr, maximum, suffix, len(arr) - 1))

    return m, n


A = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subsort(A))
