class Candy:
    def __init__(self, candy):
        self.candy = candy

    def ans(self):
        return self.candy // 10

n = int(input())
candy = Candy(n)
print(candy.ans())