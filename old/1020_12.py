class Len:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        x = len(self.a)
        y = len(self.b)
        if x == y:
            return "Yes"
        return "No"

a = input()
b = input()

len_ = Len(a, b)
print(len_.ans())
