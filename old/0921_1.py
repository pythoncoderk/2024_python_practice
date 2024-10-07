n, m = map(int, input().split())
p = int(input())
l = list(map(int, input().split()))
l2 = []
for i in range(len(l)):
    if l[i] % n == 0:
        l2.append(l[i])

min_l = max(l2)
for i in range(m):
    x = int(input())
    if abs(x - l2[i]) < min_l:
        min_l = l2[i]
    print(min_l)
    min_l = max(l2)