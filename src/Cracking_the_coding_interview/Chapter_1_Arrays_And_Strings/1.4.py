def is_palindrome_permutation(s):
    """
    Space: O(n)
    Time: O(n)
    :param s: the stringy
    :return: is it a permutation of a palindrome?
    """

    # a palindrome is a string with even numbers of every character except up to 1
    letters = 'qwertyuiopasdfghjklzxcvbnm'

    counter = dict()
    for c in letters:
        counter[c] = 0

    for c in s.lower():
        if counter.get(c) is not None:
            counter[c] += 1

    return len(list(filter(lambda x: x % 2 == 1, counter.values()))) < 2


tests = ['', 'bob', 'Tact Coa', 'bobbbobb', 'rraammm', 'onomatopeia']
for test in tests:
    print(test, is_palindrome_permutation(test))
