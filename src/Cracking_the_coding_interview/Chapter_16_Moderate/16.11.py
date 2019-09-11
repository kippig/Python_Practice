# Diving Board: You are building a diving board by placing a bunch of planks of wood end-to-end. There are two types of
# planks, one of length shorter and one of length longer. You must use exactly K planks of wood. Write a method to
# generate all possible lengths for the diving board.


def diving_board(len1, len2, K):
    """
    :param len1: size of plank 1
    :param len2: size of plank 2
    :param K: number of planks
    :return: list of possible lengths
    """
    if len1 == len2:
        return {K*len1}
    return {len1 * (K-i) + len2 * i for i in range(K + 1)}


print(diving_board(5, 10, 10))