class User:
    def __init__(self, nickname, old, birth, state):
        self.nickname = nickname
        self.old = old
        self.birth = birth
        self.state = state


n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
l2 = sorted(l, key=lambda x: x[1])

print(l)
print(l2)

