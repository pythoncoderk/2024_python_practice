n = int(input())
k = int(input())
x = int(input())
y = int(input())

if n >= k:
    x2 = k * x
else:
    x2 = n * x

if n > k:
    y2 = (n - k) * y
else:
    y2 = 0

print(x2 + y2)