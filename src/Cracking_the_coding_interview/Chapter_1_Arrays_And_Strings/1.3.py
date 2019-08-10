def URLify(s):
    """
    Space: O(1)
    Time: O(n)
    :param s: a string to turn into a URL
    :return: said URL
    """

    return s.replace(" ", "%20")