

# generate combinations:
# 1 pick smallest
# 3, 5, 7
# 3^2, 3*5, 3*7, 5*5, 5*7, 7*7 = 9, 15, 21, 25, 35, 49
# 3^3, 3^2*5, 3^2 * 7, 3*5^2, 3*5*7, 3*7^2, 5^3, 5^2*7, 5*7^2, 7^3 = 27, 45, 63, 75, 105, 147, 125, 175, 245, 343
#  84,

# 1
#    buffer 3, 5, 7, generate and check next row: 9 - 49
# 1, 3, 5, 7 because 7 < 9 (push everything less than 9)
#    buffer 9, 15, 21, 25, 35, 49, generate and check next row: 27 - 343
# 1, 3, 5, 7, 9, 15, 21, 25  (push everything less than 27). merge the rest? 27, 35, 45, 49,


def kth(k):
    """
    Time: O(k log k) <- probably faster on average with merge sort since the list is partially sorted
    Space: O(k)
    """

    numbers = []
    for a in range(k):
        for b in range(k-a):
            for c in range(k-a-b):
                numbers.append(3**a * 5**b * 7**c)
    numbers.sort()
    return numbers[k - 1]


print(kth(4))