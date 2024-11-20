n = input()

a = False
b = False
c = False
if n.count("1") == 1:
    a = True

if n.count("2") == 2:
    b = True

if n.count("3") == 3:
    c = True

print("Yes" if a and b and c else "No")

