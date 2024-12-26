n, m = map(int, input().split())

l = [["-" for j in range(n)] for i in range(n)]

l2 = [list(map(int, input().split())) for i in range(m)]

for i in range(m):
    for j in range(m):
        l2[i][j] -= 1
print(l2)


for i in range(m):
    for j in range(m):
        ll2[i][j]








