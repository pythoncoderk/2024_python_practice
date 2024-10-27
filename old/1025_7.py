class Apple:
    def __init__(self, apple):
        self.apple = apple

    def ans(self):
        return self.apple + 10

n = int(input())
apple = Apple(n)
print(apple.ans())