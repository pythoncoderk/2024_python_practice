s = list(map(str, input().split()))
a = list(map(int, input().split()))
u = input()
d = dict(zip(s, a))
# print(d)

d[u] -= 1

ans = list(d.values())
print(*ans)