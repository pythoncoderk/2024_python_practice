class Total:
    def __init__(self, tall):
        self.tall = tall

    def ans(self):
        return self.tall + 10

n = int(input())
total = Total(n)
print(total.ans())