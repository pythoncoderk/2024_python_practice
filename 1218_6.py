x = input()

y = int(x[:x.find(".")])

z = int(x[x.find(".") + 1])
print(y + 1 if z >= 5 else y)