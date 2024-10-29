class Candy:
    def __init__(self, total, candy):
        self.total = total
        self.candy = candy

    def ans(self):
        return self.total % self.candy

n, m = map(int, input().split())
candy = Candy(n, m)
print(candy.ans())