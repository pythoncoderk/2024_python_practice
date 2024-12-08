h, w = map(int, input().split())
l = [list(input()) for i in range(h)]

for i in range(h):
    l[i].append("#")
    l[i].insert(0, "#")

l.append(["#"] * (w+2))
l.insert(0, ["#"] * (w+2))

xx = 1
for q in range(h+2):
    flag = True
    for i in range(h+2):
        for j in range(w+2):
            if l[i][j] == ".":
                if flag == False:
                    break
                if l[i - 1][j] == "#" and l[i + 1][j] == "#" or l[i][j - 1] == "#" or l[i][j + 1] == "#":
                    l[i][j] = xx
                    flag = False
                elif l[i - 1][j] == "." or l[i + 1][j] == "." or l[i][j - 1] == "." or l[i][j + 1] == "." or l[i - 1][j] == xx or l[i + 1][j] == xx or l[i][j - 1] == xx or l[i][j + 1] == xx:
                    l[i][j] = xx
    xx += 1

print(l)





