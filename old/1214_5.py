a, b = map(int, input().split())

print(a * 2 + 100 - b if a * 2 + 100 > b else 0)