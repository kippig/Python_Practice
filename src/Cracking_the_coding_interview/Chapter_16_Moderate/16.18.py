def pattern_matching(value: str, pattern: str):

    # degenerate cases
    if pattern == 'a'\
            or pattern == 'b' \
            or (pattern == 'ab' and len(value) > 1) \
            or (pattern == '' and len(value) == 0):
        return True
    elif pattern == 'ab' and len(value) <= 1 or (pattern == '' and len(value) != 0):
        return False

    # check if there are multiple of the first letter
    if pattern[0] not in pattern[1:]:
        # There must be multiple of the other, so let's reverse
        value = value[::-1]
        pattern = pattern[::-1]

    # guarantee first letter is a
    if pattern[0] == 'b':
        pattern = pattern.replace('b', 'A')
        pattern = pattern.replace('a', 'b')
        pattern = pattern.replace('A', 'a')

    # we have now normalized the problem so that the first letter is a, and a occurs multiple times
    a = pattern[0]


    return pattern

value = 'catcatcatgocatgo'
pattern = 'bbbabab'
print(pattern_matching(value, pattern))