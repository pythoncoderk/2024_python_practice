def dfs(pos):
    print(pos, end=" ")
    for i in l[pos]:
        dfs(i)


h, w, d = map(int, input().split())
l = [list(input()) for i in range(h)]

for i in range(h):
    for j in range(w):
        if l[i][j] == ".":
            l[i][j] = 1
        else:
            l[i][j] = 0

print(dfs(0))



