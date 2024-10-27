class Flower:
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def total_price(self):
        return self.n * self.p

n = int(input())
p = int(input())

flower = Flower(n, p)
print(flower.total_price())