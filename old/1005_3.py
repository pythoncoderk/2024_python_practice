n = int(input())


def pulus_one(x):
    if x == 1:
        return 1
    else:
        return x + pulus_one(x - 1)

print(pulus_one(n))