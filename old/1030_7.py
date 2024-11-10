a, b = map(int, input().split())
x = a + b

if x % 3 == 0:
    print("Possible")
elif a % 3 == 0:
    print("Possible")
elif b % 3 == 0:
    print("Possible")
else:
    print("Impossible")