n = int(input())

if n % 1000 == 0:
    print(0)
elif n >= 1000:
    print(1000 - (n % 1000))
else:
    print(1000 - n)
