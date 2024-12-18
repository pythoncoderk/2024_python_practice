class Test:
    def __init__(self, name, age, bir, fro):
        self.name = name
        self.age = age
        self.bir = bir
        self.fro = fro

    def ans(self):
        print("User{")
        print(f"nickname : {self.name}")
        print(f"old : {self.age}")
        print(f"birth : {self.bir}")
        print(f"state : {self.fro}")
        print("}")

n = int(input())
for i in range(n):
    a, b, c, d = map(str, input().split())
    test = Test(a, b, c, d)
    test.ans()