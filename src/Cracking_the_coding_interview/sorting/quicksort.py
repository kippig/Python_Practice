from random import randint

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


def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p)
        quicksort(arr, p+1, high)


wrong = 0
for i in range(1000):
    arr = [randint(0, 9) for i in range(randint(1, 10))]
    quicksort(arr)
    if not arr == sorted(arr):
        wrong += 1
print(wrong/1000)

