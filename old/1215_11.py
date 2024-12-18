a, b, c, d = map(int, input().split())

print(b * c + (a - b) * d if a >= b else a * c)