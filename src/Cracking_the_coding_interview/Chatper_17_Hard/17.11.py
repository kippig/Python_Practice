def word_distance(file, w1, w2):
    """
    Time: O(n) for splitting + O(n) for traversal
    Space: O(n) for splitting into array
    """
    arr = file.split(' ')
    minimum_distance = len(arr)
    w1_pointer, w2_pointer = None, None
    for i in range(len(arr)):
        if arr[i] == w1:
            w1_pointer = i
            if w1_pointer is not None and w2_pointer is not None:
                minimum_distance = min(w1_pointer - w2_pointer, minimum_distance)
        elif arr[i] == w2:
            w2_pointer = i
            if w1_pointer is not None and w2_pointer is not None:
                minimum_distance = min(w2_pointer - w1_pointer, minimum_distance)
    return minimum_distance if minimum_distance < len(arr) else None


print(word_distance('The grey brown fox quickly jumps over the zinc', 'zinc', 'fox'))
