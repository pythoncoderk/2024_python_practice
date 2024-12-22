h, w, x, y = map(int, input().split())

l = [list(input()) for _ in range(h)]

t = list(input())
#
# print(h, w, x, y)
# print(l)
# print(t)

x, y = x - 1, y - 1
at_count = 0

for i in range(len(t)):
    if t[i] == "U":
        if l[x - 1][y] == ".":
            x -= 1
        elif l[x - 1][y] == "@":
            l[x - 1][y] = "."
            x -= 1
            at_count += 1
    elif t[i] == "D":
        if l[x + 1][y] == ".":
            x += 1
        elif l[x + 1][y] == "@":
            l[x + 1][y] = "."
            x += 1
            at_count += 1
    elif t[i] == "L":
        if l[x][y - 1] == ".":
            y -= 1
        elif l[x][y - 1] == "@":
            l[x][y - 1] = "."
            y -= 1
            at_count += 1
    elif t[i] == "R":
        if l[x][y + 1] == ".":
            y += 1
        elif l[x][y + 1] == "@":
            l[x][y + 1] = "."
            y += 1
            at_count += 1
print(x + 1, y + 1, at_count)
