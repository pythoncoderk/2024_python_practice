n = int(input())

class Times:
    def __init__(self, time):
        self.time = time

    def ans(self):
        return 60 - self.time

times = Times(n)
print(times.ans())