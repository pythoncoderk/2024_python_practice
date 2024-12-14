x, y = map(int, input().split())
top = ""
if x > y:
    top = "x"
else:
    top = "y"

if top == "x":
    print("Yes" if y + 3 > x else "No")
else:
    print("Yes" if x + 3 > y else "No")