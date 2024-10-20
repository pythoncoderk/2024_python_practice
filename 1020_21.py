class Pulus:
    def __init__(self, s_1, s_2):
        self.s_1 = s_1
        self.s_2 = s_2

    def out_put(self):
        return self.s_2 + self.s_1 + self.s_2

a = input()
b = input()

pulus = Pulus(a, b)
print(pulus.out_put())