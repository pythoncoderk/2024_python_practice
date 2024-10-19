s = input()
c = input()

class Name:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def ans(self):
        return self.num1 + self.num2

soft_name = Name(s, c)
print(soft_name.ans())