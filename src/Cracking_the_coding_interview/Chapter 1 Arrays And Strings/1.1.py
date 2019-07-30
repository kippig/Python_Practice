def unique(arr):
    """Space: O(n), Time: O(n)"""
    values = dict()
    for item in arr:
        if values.get(item) is not None:
            return False
        else:
            values[item] = 1
    return True

def unique_2(arr):
    """Without additional data structures or hash map
    Space: 1
    Time: O(n log n) """
    arr = sorted(arr)
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1]:
            return False
    return True


tests = ['', 'bob', 'bo', 'ƒœ∑´´œ¬']
for test in tests:
    print(test, unique(test), 'unique')
    print(test, unique_2(test), 'unique_2')
