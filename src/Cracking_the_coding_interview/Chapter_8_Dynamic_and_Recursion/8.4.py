from functools import reduce


def power_set(s: set):
    set_sizes = [None]*(len(s) + 1)
    set_sizes[0] = set({frozenset()})
    for size in range(1, len(s) + 1):
        set_sizes[size] = set()
        for element in s:
            for size_down in set_sizes[size - 1]:
                set_sizes[size].add(size_down.union(frozenset((element,))))
    return reduce(lambda x, y: x.union(y), set_sizes)


print(power_set({0, 1, 2, 3, 4}))

