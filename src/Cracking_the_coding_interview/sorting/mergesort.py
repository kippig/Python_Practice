def merge(arr1, arr2):
    if arr1 is None:
        return arr2
    if arr2 is None:
        return arr1

    output = [None] * (len(arr1) + len(arr2))
    p1, p2 = 0, 0
    for i in range(len(output)):
        if p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] <= arr2[p2]:
                output[i] = arr1[p1]
                p1 += 1
            else:
                output[i] = arr2[p2]
                p2 += 1
        elif p1 >= len(arr1):
            output[i:] = arr2[p2:]
            break
        else:
            output[i:] = arr1[p1:]
            break
    return output


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))


print(merge_sort([6, 7, 3, 1, 5]))

