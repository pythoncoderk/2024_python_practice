a, b, c, d = map(int, input().split())

x = a * b
y = c * d

print(x if x > y else y)