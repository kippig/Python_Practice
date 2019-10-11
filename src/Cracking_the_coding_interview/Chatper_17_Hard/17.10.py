def partition(arr, low, high):
    pivot = arr[low + (high - low)//2]
    while True:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low >= high:
            return high
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1


def find_kth(arr, k, lower=0, upper=None):
    if upper is None:
        upper = len(arr) - 1
    while True:
        if lower == upper:
            return arr[lower]

        pivot = partition(arr, lower, upper)
        if k == pivot:
            return arr[pivot]
        elif k < pivot:
            upper -= 1
        else:
            lower += 1


def median(arr):
    if len(arr) % 2 == 1:
        return find_kth(arr, len(arr)//2 + 1)
    else:
        return (find_kth(arr, len(arr)//2 - 1) + find_kth(arr, len(arr)//2))/2


def majority_element(arr):
    """
    Time: O(n)
    Space: O(1)
    """
    m = median(arr)
    counter = 0
    for i in range(len(arr)):
        if arr[i] == m:
            counter += 1
    if counter > len(arr)//2:
        return m
    return -1


a = [1, 2, 9, 9, 9, 9, 5, 5, 9]
print(majority_element(a))
