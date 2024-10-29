class Food:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        if self.a > self.b:
            return self.a
        return self.b

n = int(input())
m = int(input())
food = Food(n, m)
print(food.ans())