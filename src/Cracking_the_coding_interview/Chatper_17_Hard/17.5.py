def encode(x):
    if isinstance(x, int):
        return 0
    else:
        return 1


def letters_and_numbers(arr):
    """
    Time: O(n^2)
    Space: O(n)
    """
    maximum = -1
    pointers = (0, 0)
    encoded_arr = list(map(encode, arr))
    count_letters = sum(encoded_arr)
    count_numbers = len(encoded_arr) - count_letters

    counter= 0
    for i in range(len(arr)):
        endpoint = min(i + 2 * min(count_letters, count_numbers), len(arr))
        endpoint = endpoint - endpoint % 2 # must be even length
        temp_arr = encoded_arr[i: endpoint]
        while sum(temp_arr) != len(temp_arr)/2 and endpoint >= 0 and len(temp_arr) > maximum:
            endpoint -= 2
            temp_arr = encoded_arr[i: endpoint]
            counter += 1
        if len(temp_arr) > maximum and sum(temp_arr) == len(temp_arr)/2:
            maximum = len(temp_arr)
            pointers = (i, endpoint)

    print(counter)
    return arr[pointers[0]: pointers[1]]


arr = [0, 'a', 'b', 0, 'c', 0, 0, 0, 'd', 'e', 'f', 0, 0, 'g', 0, 0, 0, 0, 0, 0, 'h']
print(letters_and_numbers(arr))




