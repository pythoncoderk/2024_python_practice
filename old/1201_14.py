def hello(to):
    print("hello {0}".format(to))


hello("inside")

greet = hello
greet("second")


def ans(x):
    return "test {0}".format(x)

print(ans("unko"))

ans_002 = ans
print(ans_002("ikeru?"))