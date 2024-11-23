class Change:
    def __init__(self, n):
        self.n = n

    def ans(self):
        x = 1
        total = 0
        for i in range(len(self.n) - 1, -1, -1):


            if self.n[i] == "1":
                total += x
            x *= 2
        return total
n = input()
change = Change(n)
print(change.ans())
