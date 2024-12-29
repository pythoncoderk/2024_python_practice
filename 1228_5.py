l2 = list(map(int, input().split()))

l = []
for i in range(4):
    l.append(l2.count(l2[i]))
l.sort()


if (l[0] == 1 and l[1] == 3 and l[2] == 3 and l[3] == 3) or (l[0] == 2 and l[1] == 2 and l[2] == 2 and l[3] == 2):
    print("Yes")
else:
    print("No")