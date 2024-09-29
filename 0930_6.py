


def thrice(x):
    return x * 3


def quadruple(x):
    return x * 4


def thrice_and_quadruple(x):
    return quadruple(thrice(x))
print(thrice_and_quadruple(2))