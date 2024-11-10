n, q = map(int, input().split())

l = list(map(int, input().split()))

l2 = []
x = 0
for i in range(len(l)):
    l2.append(x + l[i])
    x += l[i]
l2.insert(0, 0)

for i in range(q):
    x, y = map(int, input().split())
    x -= 1
    print(l2[y] - l2[x])