import random

def shuffle(arr):
    """
    Time: O(N^2)
    Space: O(N)
    """
    scramble_set = set(range(len(arr)))
    output = [None]*len(arr)

    for i in range(len(arr)):
        x = random.sample(scramble_set, 1)[0]
        scramble_set.remove(x)
        output[x] = arr[i]

    return output


print(shuffle(list(range(52))))

