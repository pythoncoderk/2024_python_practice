class City:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        a_2 = self.a - 100
        b_2 = self.b + 100
        print(a_2)
        print(b_2)

a = int(input())
b = int(input())
city = City(a, b)
city.ans()
