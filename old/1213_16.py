h, w, n = map(int, input().split())

l1 = []
for i in range(n):
    lx = []
    for j in range(h):
        lx.append(input())
    l1.append(lx)

print(l1)

a, b = map(int, input().split())
l3 = [list(map(int, input().split())) for i in range(a)]

# print(l3)

for i in range(a):
    l_f = [[] for _ in range(h)]
    for j in range(b):
        for q in range(b):
            if len(l_f) == 1:
                l_f.append(l1[l3[i][q] - 1])
            else:
                l_f[q].append(l1[l3[i][j] - 1][q])
    for xx in range(len(l_f)):
        print("".join(l_f[xx]))

