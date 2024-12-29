n, m = map(int, input().split())

l = [list(map(int, input().split())) for i in range(m)]

l2 = [["-" for i in range(n)] for i in range(n)]

for i in range(m):
    for j in range(2):
        l[i][j] -= 1

for i in range(m):
    l2[l[i][0]][l[i][1]] = "o"
    l2[l[i][1]][l[i][0]] = "x"

for i in l2:
    print(*i)