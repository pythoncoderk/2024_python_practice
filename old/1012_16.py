import math

n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]
total = 0
x, y = 0, 0
for i in range(n):
    x1, y1 = l[i][0], l[i][1]
    total += math.sqrt(((x - x1) ** 2) + ((y - y1) ** 2))
    x, y = x1, y1

total += math.sqrt(((x - 0) ** 2) + ((y - 0) ** 2))

print(total)