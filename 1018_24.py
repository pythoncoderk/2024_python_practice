n = int(input())
l = list(map(int, input().split()))
x = int(input())

index_l = 0
chk = False
for i in range(n):
    if l[i] == x:
        index_l = i + 1
        chk = True
        break

print(index_l if chk else 0)