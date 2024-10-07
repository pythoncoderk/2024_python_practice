m, p, q = map(int, input().split())

x = m * (p / 100)
y = m - x

x2 = y * (q / 100)
y2 = y - x2

print(y2)