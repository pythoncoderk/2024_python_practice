class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def get_number(self):
        return self.number

    def get_name(self):
        return self.name

l = []
n = int(input())
for i in range(n):
    input_l = list(map(str, input().split()))
    if input_l[0] == "make":
        l.append([int(input_l[1]), input_l[2]])
    elif input_l[0] == "getnum":
        print(l[int(input_l[0])])
    else:
        print(l[int(input_l[1])])