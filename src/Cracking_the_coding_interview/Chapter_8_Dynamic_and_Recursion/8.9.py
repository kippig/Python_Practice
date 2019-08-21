def parens(n):

    def go(counter):
        if counter == [0, 1]:
            yield ')'

        for i in (0, 1):
            if counter[i] > 0 and (i == 0 or counter[1] > counter[0]):
                counter[i] -= 1
                for smaller_permutation in go(counter):
                    yield chr_map[i] + smaller_permutation
                counter[i] += 1

    counter = [n, n]  # counts '(', ')'
    chr_map = ('(', ')')
    return list(go(counter))
    # the main rule is we cannot add a ) unless there are one or more unaccounted '('


print(parens(3))