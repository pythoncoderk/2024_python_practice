n = int(input())
l = list(map(int, input().split()))

for i in range(n - 1):
    min_l = l[i]
    index_l = i
    for j in range(i, n):
        if min_l > l[j]:
            min_l = l[j]
            index_l = j
    l[i], l[index_l] = l[index_l], l[i]
    print(*l)