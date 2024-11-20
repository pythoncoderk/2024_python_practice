n, k = map(int, input().split())
s = list(input())

ans = 0

for i in range(n - k + 1):
    o_count = 0
    l = []
    for j in range(k):
        if s[i + j] == "O":
            o_count += 1
            l.append(i + j)
    if o_count == k:
        for z in range(len(l)):
            s[l[z]] = "*"
        ans += 1
print(ans)

