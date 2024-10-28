class Food:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        if self.a > self.b:
            return self.a
        return self.b

a = int(input())
b = int(input())
food = Food(a, b)
print(food.ans())