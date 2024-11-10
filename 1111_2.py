d = int(input())
n = int(input())

l = [0] * d + [0]

for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, y + 1):
        l[j] += 1

for i in range(d + 1):
    if i != 0:
        print(l[i])