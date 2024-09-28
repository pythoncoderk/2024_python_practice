class User(object):
    def __init__(self, nickname, old, birth, state):
        self.nickname = nickname
        self.old = old
        self.birth = birth
        self.state = state


n, k = map(int, input().split())
l = [list(map(str, input().split())) for i in range(n)]
l2 = [list(map(str, input().split())) for i in range(k)]
for i in range(len(l2)):
    l2[i][0] = int(l2[i][0])


def changeName(num1, num2):
    num2 = num1
    return num1

for i in range(k):
    for j in range(n):
        if l2[i][0] == j + 1:
            l[j][0] = changeName(l2[i][1], l[i][0])
            break

for i in range(n):
    x = User(l[i][0], l[i][1], l[i][2], l[i][3])
    print(x.nickname, x.old, x.birth, x.state)