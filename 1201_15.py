def calc(a, b, op="+"):
    if op not in "+-*/":
        return
    print(eval("{0} {1} {2}".format(a, op, b)))

calc(1, 1)

calc(5, 6, "*")

calc(1, op="*", b=0.5)