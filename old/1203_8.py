a, b, c = map(int, input().split())

x = a - b
y = c - x

print(y if y > 0 else 0)