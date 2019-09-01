def sort(iterable):
    arr = list(iterable)
    for inserter in range(len(arr)):
        minimum = (inserter, arr[inserter])
        for i in range(inserter, len(arr)):
            if arr[i] < minimum[1]:
                minimum = (i, arr[i])
        arr[inserter], arr[minimum[0]] = minimum[1], arr[inserter]

    return arr


print(sort('webajaljs'))
