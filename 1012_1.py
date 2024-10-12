h, w, n = map(int, input().split())
l1 = [list(input()) for _ in range(h)]

for i in range(n):
    y, x = map(int, input().split())
    l1[y][x] = "#"

for i in range(h):
    print("".join(l1[i]))