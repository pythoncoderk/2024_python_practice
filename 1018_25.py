n = int(input())
l = list(map(int, input().split()))
x = int(input())

index_l = 0
for i in range(n):
    if l[i] == x:
        index_l = i + 1

print(index_l)