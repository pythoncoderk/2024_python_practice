x, a, b = map(int, input().split())

n = abs(x - a)
m = abs(x - b)

print("A" if n < m else "B")