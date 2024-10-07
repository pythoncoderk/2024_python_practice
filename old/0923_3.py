l = list(map(int, input().split()))
c = l.pop(-1)
l.sort()

# print(c)
# print(l)

x = c // l[0]
y = c % l[0]

x2 = y // l[1]

print(x + x2)

