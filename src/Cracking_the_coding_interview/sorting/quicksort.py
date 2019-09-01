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


arr = [6, 7, 3, 1, 5]
quicksort(arr)
print(arr)

