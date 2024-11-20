s = list(input())

l = []
count = 0
for i in range(1, len(s)):
    if s[i] == "-":
        count += 1
    else:
        l.append(count)
        count = 0

print(*l)