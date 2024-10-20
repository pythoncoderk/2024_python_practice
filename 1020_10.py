n = int(input())
m = int(input())

class Drag:
    def __init__(self, days, drag):
        self.days = days
        self.drag = drag

    def ans(self):
        return self.days * self.drag * 3

week_day = Drag(n, m)
print(week_day.ans())