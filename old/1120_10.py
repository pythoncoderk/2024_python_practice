l = list(map(int, input().split()))
l.sort()

# print(l)

print(abs(l[0] - l[1]) + abs(l[1] - l[2]))

