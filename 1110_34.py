import numpy as np

n, q = map(int, input().split())
l = list(map(int, input().split()))

s = np.cumsum(l)
s = np.append(0, s)

for i in range(q):
    x, y = map(int, input().split())
    print(s[y] - s[x - 1])