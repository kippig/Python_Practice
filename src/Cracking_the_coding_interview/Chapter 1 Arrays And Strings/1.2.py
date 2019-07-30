def same_chars(s1, s2):
    """
    Space: O(n)
    Time: O(n)
    :param s1: String1
    :param s2: String2
    :return: Are the strings permutations of each other?
    """

    # Sort the two strings then are they equal O(n log n + k log k) space (1)
    # Put s1 in a hash table then compare to string2

    if len(s2) != len(s1):
        return False

    s1_hash = dict()
    for c in s1:
        if s1_hash.get(c) is None:
            s1_hash[c] = 1
        else:
            s1_hash[c] += 1

    for c in s2:
        if s1_hash.get(c) is None:
            return False
        elif s1_hash[c] == 0:
            return False
        else:
            s1_hash[c] = s1_hash[c] - 1
    return True


tests = [('bob', 'bbo'), ('bob', ''), ('face', 'pigg')]
for test in tests:
    print(test, same_chars(*test))
