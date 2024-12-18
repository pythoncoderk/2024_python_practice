n, m, l = map(str, input().split())
n = int(n)
s = list(input())

for i in range(n):
    if s[i] != m:
        s[i] = l

print("".join(s))