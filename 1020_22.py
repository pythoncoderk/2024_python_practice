class Games:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        return self.a - self.b

a = int(input())
b = int(input())
games = Games(a, b)
print(games.ans())