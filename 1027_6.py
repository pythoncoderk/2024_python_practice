class Shopping:
    def __init__(self, check):
        self.check = check

    def ans(self):
        if self.check >= 1000:
            return "Yes"
        return "No"
n = int(input())
b_kun_shopping = Shopping(n)
print(b_kun_shopping.ans())