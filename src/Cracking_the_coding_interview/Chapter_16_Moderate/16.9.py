# waste of time
def multiply(a, b):
    """a * b"""
    product = 0
    for i in range(a):
        product += b
    return product


def division(a, b):
    """a //b"""
    counter = 0
    divisor = b
    while divisor <= a:
        counter += 1
        divisor += b
    return counter


def subtract(a, b):
    """a - b, only valid if a is greater than b"""
    counter = 0
    if b > 0:
        for i in range(b):
            counter += -1
    else:
        for i in range():
            pass


print(subtract(100, 2))
