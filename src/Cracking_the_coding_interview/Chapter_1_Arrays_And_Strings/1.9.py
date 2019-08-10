def string_rotation(s1, s2):
    """
    Space: O(M), M = len(s2)
    Time: O(M)
    :param s1:
    :param s2:
    :return:
    """
    if len(s1) == len(s2):
        return s1 in ''.join((s2, s2))
    else:
        return False


tests = [ ('waterbottle', 'erbottlewat'),
          ('rhubarb', 'barbrhu'),
          ('yuki', 'pelin')]

for test in tests:
    print(test, string_rotation(*test))
