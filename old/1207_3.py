n = int(input())

l = 0
nex = 0
for i in range(n):
    if i == 0:
        x, y = map(int, input().split())
        nex = x
        l += y
    else:
        x, y = map(int, input().split())
        l -= x - nex
        if l < 0:
            l = 0
        nex = x
        l += y

print(l)


