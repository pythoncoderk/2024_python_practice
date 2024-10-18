n = int(input())
l = list(map(int, input().split()))
k = int(input())

count = max(l)
for i in range(n):
    if l[i] >= k:
        count = min(count, l[i])

print(count)
