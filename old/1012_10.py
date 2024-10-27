class Paper:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def ans(self):
        return self.h * self.w


h, w = map(int, input().split())
paper = Paper(h, w)
print(paper.ans())