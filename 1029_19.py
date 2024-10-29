x, a, b = map(int, input().split())

y = b - a

if y <= 0:
    print("delicious")
elif x >= y:
    print("safe")
else:
    print("dangerous")