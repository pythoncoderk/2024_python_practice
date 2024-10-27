class Get:
    def __init__(self, total, get):
        self.total = total
        self.get = get

    def ans(self):
        return self.total - self.get


a = int(input())
b = int(input())


answer = Get(a, b)
print(answer.ans())