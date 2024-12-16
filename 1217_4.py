a, b, c = map(int, input().split())

x = ((a + c - 1) // c) * c

print(x if a <= x <= b else -1)
