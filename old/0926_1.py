n, m = map(int, input().split())

x = abs(n - m)
y = abs(m - 1)

print(x if x < y else y)