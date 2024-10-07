def thrice(x):
    return x * 3


def quadruple(x):
    return x * 4

# 以下のコードを修正
def thrice_and_quadruple(x):
    x = thrice(x)
    return quadruple(x)


print(thrice_and_quadruple(2))
