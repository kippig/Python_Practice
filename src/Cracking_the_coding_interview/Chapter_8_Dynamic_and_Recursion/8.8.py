def permutations(iterable):
    """"""
    if len(iterable) == 1:
        yield iterable

    for i in range(len(iterable)):
        for smaller_permuation in permutations(iterable[:i] + iterable[i + 1:]):
            yield iterable[i] + smaller_permuation


def dedup_permutations(iterable):
    return set(permutations(iterable))


def dedup_permutations2(iterable, hashmap=None):
    if hashmap is None:
        hashmap = dict()
        for character in iterable:
            if hashmap.get(character) is None:
                hashmap[character] = 1
            else:
                hashmap[character] += 1

    if sum(hashmap.values()) == 1:
        for key in hashmap.keys():
            if hashmap[key] == 1:
                yield key

    for key in hashmap.keys():
        if hashmap[key] > 0:
            hashmap[key] -= 1
            for smaller_permutation in dedup_permutations2(None, hashmap):
                yield key + smaller_permutation
            hashmap[key] += 1


print(list(dedup_permutations2('12444')))
