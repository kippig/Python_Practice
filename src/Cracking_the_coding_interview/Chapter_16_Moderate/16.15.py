def mastermind_checker(guess, solution):
    """

    :param guess:
    :param solution:
    :return: hits, pseudo-hits
    """
    hits = 0
    extant_colours = set(solution)
    pseudohits = set()
    for i in range(4):
        if guess[i] == solution[i]:
            hits += 1
        elif guess[i] in extant_colours:
            pseudohits.add(guess[i])
    return hits, len(pseudohits)


print(mastermind_checker('GGRR', 'RGBY'))
