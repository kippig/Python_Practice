def triple_step(steps=10):
    """f(n) = f(n-1) + f(n-2) + f(n-3) + 1"""
    memo = [None] * steps
    memo[0], memo[1], memo[2] = 1, 2, 4
    if steps < 3:
        return memo[steps]

    for i in range(3, steps):
        memo[i] = 1 + memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[-1]


print(triple_step(1000))
