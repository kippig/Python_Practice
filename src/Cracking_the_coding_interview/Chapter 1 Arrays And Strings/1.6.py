def string_compression(s):
    """
    Space: O(n)
    Time: O(n)
    :param s:
    :return:
    """

    if len(s) == 0: return s

    compressed_s = ""
    counter = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i-1]:
            counter += 1
        else:
            compressed_s = ''.join((compressed_s, s[i-1], str(counter)))
            counter = 1

    if len(compressed_s) > len(s):
        return s
    else:
        return compressed_s


tests = ['', 'bob', 'aasdsssssiiiiiiiii', 'abdcedf', 'aaabcdefghhijk']
for test in tests:
    print(test, string_compression(test))
