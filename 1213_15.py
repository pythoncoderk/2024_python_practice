n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
l2 = list(map(int, input().split()))

# print(n, m)
# print(l)
# print(l2)

ans = 0

for q in range(m):
    for i in range(n):
        for j in range(n):
            if l2[q] == l[i][j] or l[i][j] == 0:
                l[i][j] = "*"

l3 = []
for i in range(n):
    ll = []
    for j in range(n):
        ll.append(l[j][i])
    l3.append(ll)

l4 = []
for i in range(n):
    l4.append(l[i][i])
if l4.count("*") == n:
    ans += 1

l5 = []
x = 0
for i in range(n - 1, -1, -1):
    l5.append(l[x][i])
    x += 1
if l5.count("*") == n:
    ans += 1

# print(l)
# print(l3)
# print(l4)
# print(l5)

for i in range(n):
    if l[i].count("*") == n:
        ans += 1

for i in range(n):
    if l3[i].count("*") == n:
        ans += 1

print(ans)