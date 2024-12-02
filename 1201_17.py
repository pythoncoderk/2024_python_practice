def foo(a, b, *args):
    print("TEST")
    for arg in args:
        print(arg)

foo(9, 9, 100, 101, 102)