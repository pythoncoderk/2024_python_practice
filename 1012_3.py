h, w = map(int, input().split())
l = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        x, y = i, j
        if x == 0 or l[x - 1][j] == "#":
            if x == h - 1 or l[x + 1][j] == "#":
                print(x, y)