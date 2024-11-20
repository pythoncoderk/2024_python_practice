class Week:
    def __init__(self, n):
        self.days = n

    def ans(self):
        return self.days * 7

n = int(input())
week = Week(n)
print(week.ans())