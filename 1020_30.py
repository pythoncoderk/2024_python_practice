n = int(input())
l = [list(map(str, input().split())) for _ in range(n)]

class List:
    def __init__(self, name, age, birth, address):
        self.name = name
        self.age = age
        self.birth = birth
        self.address = address

    def ans(self):
        print("User{")
        print(f"nickname : {self.name}")
        print(f"old : {self.age}")
        print(f"birth : {self.birth}")
        print(f"state : {self.address}")
        print("}")

for i in l:
    a, b, c, d = i
    list = List(a, b, c, d)
    list.ans()