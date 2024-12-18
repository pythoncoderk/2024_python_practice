a, b = map(str, input().split())

x, y, z = int(a[0]), int(a[1]), int(a[2])
n, m, l = int(b[0]), int(b[1]), int(b[2])

print(x + y + z if x + y + z > n + m + l else n + m + l)