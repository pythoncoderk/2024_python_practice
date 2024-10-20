n, k = map(int, input().split())
l1 = [list(map(str, input().split())) for _ in range(n)]
l2 = [list(map(str, input().split())) for _ in range(k)]

for i in range(k):
    l2[i][0] = int(l2[i][0])

for i in range(k):
    l1[l2[i][0] - 1][0] = l2[i][1]

for i in l1:
    print(*i)