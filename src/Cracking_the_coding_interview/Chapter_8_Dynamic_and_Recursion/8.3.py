def find_index(arr):
    """
    Space: 1
    Time: O(n) in the worst case (magic index in the middle)
    Handles duplicate values
    """

    i, j = 0, len(arr) - 1
    while True:
        if i >= len(arr) or j < 0:
            return False

        if arr[i] == i:
            return i
        elif arr[i] > i:
            i = arr[i]
        else:
            i += 1

        if arr[j] == j:
            return j
        elif arr[j] < j:
            j = arr[j]
        else:
            j -= 1


def find_index2(arr, base=0):
    """
    Space: 1
    Time: O(log n)
    """
    if len(arr) == 0:
        return None
    i = len(arr)//2
    if arr[i] < base + i:
        return find_index2(arr[i+1:], base + i + 1)
    elif arr[i] > base + i:
        return find_index2(arr[:i], base)
    else:
        return base + i


print(find_index2([-2, -1, 0, 3]))
