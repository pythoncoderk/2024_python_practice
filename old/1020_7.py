n = int(input())
m = int(input())
p = int(input())

class Trumps:
    def __init__(self, total, player, card):
        self.total = total
        self.player = player
        self.card = card

    def ans(self):
        x = self.player * self.card
        if self.total - x > 0:
            return self.total - x
        return 0
    
farst_game = Trumps(n, m, p)
print(farst_game.ans())