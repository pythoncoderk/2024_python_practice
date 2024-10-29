class Ans:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def ans(self):
        return f"{self.one}/{self.two}"

n = input()
m = input()
final_ans = Ans(n, m)
print(final_ans.ans())