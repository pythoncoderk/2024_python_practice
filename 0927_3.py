class Student(object):
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state


n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
num = input()

for i in range(n):
    a, b, c, d = l[i]
    x = Student(a, b, c, d)
    if x.old == num:
        print(x.name)