n = int(input())
l = list(map(int, input().split()))
k = int(input())

count = min(l)
for i in range(n):
    if k >= l[i]:
        count = max(count, l[i])

print(count)