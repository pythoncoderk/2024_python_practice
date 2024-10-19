a = int(input())
b = int(input())

class Total:
    def __init__(self, pants, shorts):
        self.pants = pants
        self.shorts = shorts

    def ans(self):
        return self.pants + self.shorts

total = Total(a, b)
print(total.ans())