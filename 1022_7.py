class Apple:
    def __init__(self, count):
        self.count = count

    def ans(self):
        return self.count + 10

n = int(input())
apple = Apple(n)
print(apple.ans())