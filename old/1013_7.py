class Gets:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def ans(self):
        return self.two * 2 - self.one

one = int(input())
two = int(input())

gets = Gets(one, two)
print(gets.ans())