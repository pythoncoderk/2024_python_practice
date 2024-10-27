n = int(input())

class Answer:
    def __init__(self, total):
        self.total = total

    def final(self):
        x = self.total // 80
        return x


ans = Answer(n)
print(ans.final())