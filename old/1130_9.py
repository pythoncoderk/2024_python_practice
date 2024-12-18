l = list(map(int, input().split()))
l.sort(reverse=True)

x = str(l[0]) + str(l[1])
y = int(x) + l[2]

print(y)

