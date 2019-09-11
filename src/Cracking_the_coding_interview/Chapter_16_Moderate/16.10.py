# Living People: Given a list of people with their birth and death years, implement a method to compute the year with
# the most number of people alive. You may assume that all people were born between 1900 and 2000 (inclusive). If a
# person was alive during any portion of that year, they should be included in that year's count. For example, Person
# (birth= 1908, death= 1909) is included in the counts for both 1908 and 1909.


def living_people(living_years):
    """

    :param living_years: list of tuples (birth, death) where 1900 <= birth <= death <= 2000
    :return:
    """

    counts = [0]*101
    for person in living_years:
        counts[person[0] - 1900: person[1] + 1 - 1900] = map(lambda x: x + 1,
                                                             counts[person[0] - 1900: person[1] + 1 - 1900])
    return max(enumerate(counts), key=lambda x: x[1])[0]


arr = [(1900, 2000),
       (1909, 1909)]
print(living_people(arr))
