n = int(input())
l = list(map(int, input().split()))

count = 0
for i in range(n):
    if l[i] % 2 != 0:
        count = i + 1

print(count)