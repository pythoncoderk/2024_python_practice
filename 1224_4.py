import math

x, y = map(int, input().split())

z = y - x

if z <= 0: print(0)
else: print(math.ceil(z / 10))