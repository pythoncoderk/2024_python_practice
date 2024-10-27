n = int(input())
l = list(map(int, input().split()))
x = int(input())

count = 0
for i in range(n):
    if l[i] == x:
        count += 1

print(count)