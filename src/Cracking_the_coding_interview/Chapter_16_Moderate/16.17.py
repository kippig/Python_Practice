def contiguous_sum(arr: list):
    """
    Time: O(n)
    Space: O(1)
    :param arr:
    :return: largest contiguous sum
    """

    global_max = float('-inf')
    last_round = 0
    for i in range(len(arr)):
        this_round = arr[i]
        last_round += arr[i]
        last_round = max(this_round, last_round)
        global_max = max(last_round, global_max)

    return global_max


A = [2, -8, 3, -2, 4, -10]
print(contiguous_sum(A))
