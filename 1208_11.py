h, w = map(int, input().split())
l = [list(input()) for i in range(h)]

for i in range(h):
    l[i].append("#")
    l[i].insert(0, "#")

l.append(["#"] * (w+2))
l.insert(0, ["#"] * (w+2))

# print(l)
max_l = 0
xx = 0
for q in range(h+2):
    flag = True
    flag_get = True
    xx += 1
    for i in range(h+2):

        for j in range(w+2):
            if l[i][j] == ".":
                if flag:
                    flag = False
                    l[i][j] = xx
                    max_l = xx
                    if l[i-1][j] == "." or l[i+1][j] == "." or l[i][j-1] == "." or l[i][j+1] == ".":
                        flag_get = False
                else:
                    if l[i-1][j] == xx or l[i+1][j] == xx or l[i][j-1] == xx or l[i][j+1] == xx or flag_get == False:
                        l[i][j] = xx

print(max_l)
print(l)

