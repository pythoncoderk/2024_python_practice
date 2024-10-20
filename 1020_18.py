n = int(input())
l = list(map(str, input().split()))


class Member:
    def __init__(self, arr):
        self.arr[0] = arr[0]
        self.arr[1] = arr[1]
        self.arr[2] = arr[2]
        self.arr[3] = arr[3]
    def ans(self):
        print("User{")
        print(f"nickname : {self.arr[0]}")
        print(f"old : {self.arr[1]}")
        print(f"birth : {self.arr[2]}")
        print(f"state : {self.arr[3]}")
        print("}")

for i in range(n):
    member = Member(l[i])
    member.ans()