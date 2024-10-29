class Kyebord:
    def __init__(self, n):
        self.n = n

    def ans(self):
        return self.n * 365

n = int(input())
keybord = Kyebord(n)
print(keybord.ans())