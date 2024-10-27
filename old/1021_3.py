class Employee:
    def __init__(self, a, num, name):
        self.a = a
        self.num = num
        self.name = name

    def getnum(self, num, arr):
        print(arr[num - 1][1])

    def getname(self, num, arr):
        print(arr[num - 1][0])

    def make(self, num, name, arr):
        arr.append(name, num)


l = []
n = int(input())
for i in range(n):
    input_l = list(map(str, input().split()))
    employee = Employee(input_l[0], input_l[1], input_l[2])
    if input_l[0] == "make":
        print("a")
