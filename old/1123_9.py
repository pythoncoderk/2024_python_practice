class Player:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def ans(self):
        return self.n // self.m

n, m = map(int, input().split())
player = Player(n, m)
print(player.ans())