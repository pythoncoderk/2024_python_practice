d = int(input())
n = int(input())

l = [0] + [0] * d + [0]

for i in range(n):
    x, y = map(int, input().split())
    l[x] += 1
    l[y + 1] -= 1

l2 = []
x = 0
for i in range(len(l)):
    l2.append(x + l[i])
    x += l[i]

for i in range(len(l2)):
    if i != 0 and i != len(l2) - 1:
        print(l2[i])
