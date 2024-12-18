class Turn:
    def __init__(self, st):
        self.st = st

    def ans(self):
        for i in range(len(self.st)):
            if i % 9 != 0 or i == 0:
                print(self.st[i], end="")
            else:
                print(self.st[i])

s = input()
turn = Turn(s)
turn.ans()