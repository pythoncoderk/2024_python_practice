import math

n, x, t = map(int, input().split())

x = math.ceil(n / x)

print(x * t)