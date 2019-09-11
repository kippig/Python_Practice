# Factorial Zeros: Write an algorithm which computes the number of trailing zeros in n factorial.

# need to count the number of multiples of 10
# need to count pairs of 2, 5

# given n, loop up 10^i adding i each time
# divide n by 10, that's how many pairs of 2, 5 there are
from math import factorial


def factorial_zeroes(n):

    # multiples of 10
    i = 10
    zeroes = 0
    while i <= n:
        step = i
        for j in range(i, i + 10):
            if i <= n:
                zeroes += len(str(i)) - 1
            else:
                break
            i += step

    # powers of 5
    i = 5
    while i <= n:
        zeroes += n//i
        i *= 5

    return zeroes


# for i in range(1000):
#     if set(str(factorial(i))[-1 * factorial_zeroes(i) + 1:]) != {'0'}:
#         print(i, set(str(factorial(i))[-1 * factorial_zeroes(i) + 1:]))

for x in range(10,1000):
    if (factorial(x) % (10**factorial_zeroes(x))) == 0:
        print(x)