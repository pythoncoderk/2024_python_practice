n, m = map(int, input().split())

l = [list(input()) for i in range(n)]

for i in range(n):
    count = 0
    for j in range(m):
        if l[i][j] == "." or l[i][j] == "*":
            count += 1

    if len(l[i]) == count:
        for q in range(m):
            l[i][q] = "*"

for i in range(m):
    count = 0
    for j in range(n):
        if l[j][i] == "." or l[j][i] == "*":
            count += 1
    if count == n:
        for q in range(n):
            l[q][i] = "*"


for i in range(n):
    for j in range(m):
        if l[i][j] != "*":
            print(l[i][j], end="")
    print()


