l = list(input())

count = 0

for i in range(len(l) - 1):
    x = ord(l[i])
    y = ord(l[i + 1])
    count += abs(x - y)

print(count)