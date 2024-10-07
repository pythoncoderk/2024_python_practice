class User(object):
    def __init__(self, nickname, old, birth, state):
        self.nickname = nickname
        self.old = old
        self.birth = birth
        self.state = state


n = int(input())
l = [list(map(str, input().split())) for _ in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])
l = sorted(l, key=lambda x: x[1])
# print(l)

for i in range(n):
    x = User(l[i][0], l[i][1], l[i][2], l[i][3])
    print(x.nickname, x.old, x.birth, x.state)