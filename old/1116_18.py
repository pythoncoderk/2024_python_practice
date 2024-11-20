n, k = map(int, input().split())
s = list(input())

for i in range(len(s)):
    s[i] = int(s[i])

print(s)

l = []
x = 0
for i in range(len(s)):
    x += s[i]
    l.append(x)


print(l)