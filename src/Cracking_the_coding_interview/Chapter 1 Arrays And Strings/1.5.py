def levenshtein_distance(s1, s2):
    """
    Space: O(n*k)
    Time: O(n*k)
    :param s1:
    :param s2:
    :return:
    """

    array_map = [[0 for x in range(len(s1))] for y in range(len(s2))]
    array_map[0][0] = int(s1[0] != s2[0])
    for col in range(1, len(s1)):
        array_map[0][col] = array_map[0][col - 1] + (s2[0] != s1[col])

    for row in range(1, len(s2)):
        array_map[row][0] = array_map[row - 1][0] + (s2[row] != s1[0])

    for row in range(1, len(s2)):
        for col in range(1, len(s1)):
            array_map[row][col] = min(array_map[row - 1][col] + 1,
                                      array_map[row][col - 1] + 1,
                                      array_map[row - 1][col - 1] + (s1[col] != s2[row]))
    return array_map[-1][-1]


def one_away(s1, s2):
    """
    Space: O(n*k), Time: O(n*k)
    :param s1:
    :param s2:
    :return:
    """
    return levenshtein_distance(s1, s2) < 2

