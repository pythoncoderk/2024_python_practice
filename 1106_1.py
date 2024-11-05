x, y = map(str, input().split())

x2 = ord(x)
y2 = ord(y)

if x2 == y2:
    print("=")
elif x2 > y2:
    print(">")
else:
    print("<")