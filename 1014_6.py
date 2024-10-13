class ChkPrice:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def jage(self):
        x = self.b * 0.7
        if self.a < x:
            return self.a
        return int(x)

a, b = map(int, input().split())
chk_price = ChkPrice(a, b)
print(chk_price.jage())