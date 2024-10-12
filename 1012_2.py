h, w = map(int, input().split())
l = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        x, y = i, j
        if y == 0:
            if l[x][j + 1] == "#":
                print(x, y)
        elif y == w - 1:
            if l[x][j - 1] == "#":
                print(x, y)
        else:
            if l[x][j + 1] == "#" and l[x][j - 1] == "#":
                print(x, y)
