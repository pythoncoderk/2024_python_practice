h, w = map(int, input().split())
l = [list(input()) for _ in range(h)]

# print(l)

for i in range(h):
    for j in range(w):
        if i == 0 or l[i - 1][j] == "#":
            if i == h - 1 or l[i + 1][j] == "#":
                if j == 0 or l[i][j - 1] == "#":
                    if j == w - 1 or l[i][j + 1] == "#":
                        print(i, j)