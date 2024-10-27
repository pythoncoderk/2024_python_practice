class Chk:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def a_and_b(self):
        if len(self.a) == len(self.b):
            return "Yes"
        else:
            return "No"

a = input()
b = input()

chk = Chk(a, b)
print(chk.a_and_b())