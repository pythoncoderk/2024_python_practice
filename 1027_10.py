class Total:
    def __init__(self, apple):
        self.apple = apple

    def ans(self):
        return self.apple * 3

n = int(input())
total = Total(n)
print(total.ans())