import math


# Complete the minimumPasses function below.
def distributed_costs(m, w, new):
    """
    new: number of new items
    """
    if abs(w - m) >= new:
        if m < w:
            m += new
        else:
            w += new
        return m, w
    new -= abs(w - m)
    return max(m, w) + new//2 + new % 2, max(m, w) + new//2


def minimumPasses(m, w, p, n, candies=0):
    steps = 1
    keep_turns = float('inf')
    while m * w + candies < n:
        keep_turns = min(math.ceil((n - candies) / (m * w)) + steps - 1, keep_turns)
        if keep_turns > 1 and p < n:
            buy_turns = math.ceil((p - candies) / (m * w))
            candies = buy_turns * m * w + candies
            buys = candies // p
            candies = candies - buys * p
            m, w = distributed_costs(m, w, buys)
            steps += buy_turns
        else:
            steps = keep_turns
            break
        print(m, w, candies)
    return min(keep_turns, steps)


print(minimumPasses(1, 1, 1000000000000, 1000000000000))

