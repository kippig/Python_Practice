def arrayManipulation(n, queries):
    arr = [0] * n
    for q in queries:
        arr[q[0] - 1] += q[2]
        if len(arr) > q[1]:
            arr[q[1]] -= q[2]

    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    return max(arr)



print(arrayManipulation(4, [[2, 3, 603], [1, 1, 286], [4, 4, 882]]))
