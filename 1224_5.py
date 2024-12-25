
def x(t):
    return t ** 2 + 2 * t + 3

t = int(input())

print(x(x(x(t) + t) + x(x(t))))

