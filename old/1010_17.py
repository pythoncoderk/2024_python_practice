t = int(input())

class Conbini:
    def __init__(self, hot):
        self.hot = hot

    def ans(self):
        x = self.hot - 10
        return x

conbi = Conbini(t)
print(conbi.ans())