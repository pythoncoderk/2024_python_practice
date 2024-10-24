class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self, number, arr):
        x = arr[int(number) - 1][0]
        return x

    def getname(self, number, arr):
        x = arr[int(number) - 1][1]
        return x

    def make_number_name(self, arr):
        arr.append([self.number, self.name])
        return arr

l = []
n = int(input())
for i in range(n):
    x = list(map(str, input().split()))
    if x[0] == "make":
        employee = Employee(int(x[1]), x[2])
        employee.make_number_name(l)
    elif x[0] == "getnum":
        employee = Employee(int(x[1]), x[0])
        print(employee.getnum(int(x[1]), l))
    else:
        employee = Employee(int(x[1]), x[0])
        print(employee.getname(int(x[1]), l))


