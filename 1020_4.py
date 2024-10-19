a, b = map(int, input().split())

class Games:
    def __init__(self, this_y, next_y):
        self.this_y = this_y
        self.next_y = next_y

    def ans(self):
        if self.this_y < self.next_y:
            return "Yes"
        return "No"

games = Games(a, b)
print(games.ans())