n = float(input())
x = str(n)[-1]
x = int(x)


if 0 <= x <= 2: print(str(n)[:str(n).find(".")] + "-")
elif 3 <= x <= 6: print(str(n)[:str(n).find(".")])
elif 7 <= x <= 9: print(str(n)[:str(n).find(".")] + "+")