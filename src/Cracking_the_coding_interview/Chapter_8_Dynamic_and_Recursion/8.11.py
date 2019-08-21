def enumerate_coins(n):
    """

    :param n:
    :return: (quarters, dimes, nickels, pennies)
    """

    ways = [0]*(n+1)
    ways[0] = 1
    for coin in (1, 5, 10, 25):
        for value in range(coin, n + 1):
            ways[value] += ways[value - coin]
    return ways[n]


print(enumerate_coins(100000))
