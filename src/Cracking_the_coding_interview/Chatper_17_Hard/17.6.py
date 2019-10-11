def count_of_2s(n):
    """
    Time: O(log n)
    Space: O( 1)
    """
    i = 1
    counter = 0
    while n >= (10**(i-1)):
        counter += (10**(i-1) * (n//10**i))
        counter += min(10**(i-1), max(n % (10**i) - 2 * 10**(i-1) + 1, 0))
        #counter += n // (10**i) + ((n % (10**i)) >= 2)
        i += 1

    print(counter)



count_of_2s(50229)


