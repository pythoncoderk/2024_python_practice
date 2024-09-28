class User(object):
    def __init__(self, nickname, old, birth, state):
        self.nickname = nickname
        self.old = old
        self.birth = birth
        self.state = state


def changename(x, y):
    x, y = y, x
    return x, y
    
n, m = map(int, input().split())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(m):
    a, b = map(str, input().split())
    a = int(a)
    if a - 1 == i:
        