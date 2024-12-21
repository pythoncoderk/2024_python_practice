a, op, b = map(str, input().split())

if op == "+": print(int(a) + int(b))
elif op == "-": print(int(a) - int(b))
elif op == "*": print(int(a) * int(b))
elif op == "/" and b == "0": print("error")
elif op == "/": print(int(a) // int(b))

else: print("error")

