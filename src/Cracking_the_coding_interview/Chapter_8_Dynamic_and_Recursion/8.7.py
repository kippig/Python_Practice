def permutations(iterable):
    """"""
    if len(iterable) == 1:
        yield iterable

    for i in range(len(iterable)):
        for smaller_permuation in permutations(iterable[:i] + iterable[i + 1:]):
            yield iterable[i] + smaller_permuation


print(list(permutations('1234')))
