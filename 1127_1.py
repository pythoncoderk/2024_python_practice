import math


class Tree:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y

    def ans(self):
        return math.ceil(self.n / self.x) * self.y

n, x, y = map(int, input().split())
tree = Tree(n, x, y)
print(tree.ans())