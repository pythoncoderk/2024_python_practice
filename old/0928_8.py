class User(object):
    def __init__(self, nickname, old, birth, state):
        self.nickname = nickname
        self.old = old
        self.birth = birth
        self.state = state


n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(len(l)):
    l[i][1] = int(l[i][1])

l2 = sorted(l, key=lambda x: x[1])

for i in range(n):
    x = User(l2[i][0], l2[i][1], l2[i][2], l2[i][3])
    print(x.nickname, x.old, x.birth, x.state)