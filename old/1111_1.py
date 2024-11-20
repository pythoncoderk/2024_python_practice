n = int(input())
l = list(map(int, input().split()))
q = int(input())
l2 = [list(map(int, input().split())) for i in range(q)]

l3 = []
x = 0
for i in range(n):
    l3.append(x + l[i])
    x += l[i]

l4 = []
x = 0
for i in range(n):
    if l[i] == 0:
        l4.append(x + 1)
        x += 1
    else:
        l4.append(x)


l3 = [0] + l3
l4 = [0] + l4

for i in range(q):
    x, y = l2[i][0], l2[i][1]
    win = l3[y] - l3[x - 1]
    lose = l4[y] - l4[x - 1]
    if win == lose:
        print("draw")
    elif win > lose:
        print("win")
    else:
        print("lose")