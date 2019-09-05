from random import randint
import statistics

# Strategy
# first find the median of the list
# Then sort the array into below median/ above median (1 level of quick sort)
# Then swap every other element between low and high. This works in the degenerate case where all values are equal.


def partition(a, l, r):
    x = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def select_kth(arr, k, left=0, right=None):
    """
    Time: O(n)
    """
    if right is None:
        right = len(arr) - 1

    while True:
        if left == right:
            return arr[left]
        pivot = partition(arr, left, right)
        # print(arr, left, right, 'pivot', pivot)
        if k == pivot:
            return arr[k]
        elif k < pivot:
            right = pivot - 1
        elif k > pivot:
            left = pivot + 1


def median(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) % 2 == 1:
        return select_kth(arr, k=len(arr)//2)
    else:
        lower = select_kth(arr, left=0, right=len(arr)-1, k=len(arr)//2 - 1)
        upper = select_kth(arr, left=0, right=len(arr)-1, k=len(arr)//2)
        return (lower + upper)/2


def peaks_and_valleys(arr):
    if len(arr) in (0, 1, 2):
        return

    pivot = median(arr)
    if len(arr) % 2 == 0:
        valley = len(arr) - 2
    else:
        valley = len(arr) - 1
    peak = 1

    while arr[valley] > pivot or arr[peak] < pivot:
        arr[valley], arr[peak] = arr[peak], arr[valley]
        valley -= 2
        peak += 2


for i in range(1000):
    arr = [randint(0, 9) for i in range(9)]
    peaks_and_valleys(arr)
    for i in range(0, len(arr) - 2, 2):
        if not (arr[i] <= arr[i + 1] and arr[i + 1] >= arr[i + 2]):
            print(arr, i)
            exit()


