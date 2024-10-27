n = int(input())
m = int(input())

class Total:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def ans(self):
        answer = self.one + self.two
        return answer

total = Total(n, m)
print(total.ans())