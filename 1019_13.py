n = int(input())
l = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(i + 1, 0, -1):
        if l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
    print(*l)