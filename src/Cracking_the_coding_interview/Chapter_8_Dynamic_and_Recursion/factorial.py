def factorial(n):
    partial_solution = 1
    for i in range(1, n):
        partial_solution = i * partial_solution
    return partial_solution


print(factorial(52))
