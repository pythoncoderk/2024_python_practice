n, c = map(int, input().split())
l = list(map(int, input().split()))

chk = True
count = 0
candy = 0
for i in range(n):
    if chk:
        candy += 1
        count = l[i]
        chk = False
    else:
        if l[i] - count >= c:
            candy += 1
            count = l[i]
            chk = False
print(candy)