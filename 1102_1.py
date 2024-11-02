n, m = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

l2 = [[0, 0] for i in range(m)]

for i in range(n):
    for j in range(m):
        if j == 0 or j % l[i][0] == 0:
            l2[j][0] += 1
            l2[j][1] += l[i][1]
ans = 0
for i in range(len(l2)):
    if l2[i][0] >= 3:
        ans += l2[i][1] - (l2[i][1] * 0.15)
    elif l2[i][0] >= 2:
        ans += l2[i][1] - (l2[i][1] * 0.1)
    else:
        ans += l2[i][1]
print(int(ans))


