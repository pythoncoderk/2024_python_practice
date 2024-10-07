n, r = map(int, input().split())

for i in range(n):
    x, y, z = map(int, input().split())
    l = [x, y, z]
    l_min = min(l)
    if l_min >= r * 2:
        print(i + 1)