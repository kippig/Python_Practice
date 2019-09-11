def smallest_difference(arr1, arr2):
    """
    Time: O(n * k) slooow
    Space: O(1)
    """
    minimum = float('inf')
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            diff = abs(arr1[i] - arr2[j])
            if diff < minimum:
                minimum = diff
                if diff == 0:
                    return 0
    return minimum


def smallest_difference2(arr1, arr2):
    """
    We could sort arr1, then for arr2, do binary search to find the closest value in arr1
    Time: O(n log n + K log n) <- very optimal if we can make n small
    Space: O(1)
    """

    def binary_search(arr, lower, upper, target):
        if lower == upper:
            return abs(target - arr[lower])
        elif upper - lower == 1:
            return min(arr[upper] - target, target - arr[lower])
        else:
            pivot = (lower + upper)//2
            if arr[pivot] > target:
                return binary_search(arr, lower, pivot, target)
            else:
                return binary_search(arr, pivot, upper, target)

    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    arr1.sort()
    minimum = float('inf')
    for member in arr2:
        diff = binary_search(arr1, 0, len(arr1) - 1, member)
        if diff < minimum:
            minimum = diff
    return diff


def smallest_difference3(arr1, arr2):
    """
    Sort arr1 and arr2  O( n log n + k log k)
    then merge sort with a tuple, when you pull from opposite lists in a row, note the difference O ( n + k)
    Time: O( n log n + k log k + n + k) = O( n log n + k log k) <- not faster than above
    Space: O(n + k)
    """


arrs = [[1, 3, 15, 11, 2],
        [23, 127, 235, 19, 8]]
print(smallest_difference2(*arrs))
