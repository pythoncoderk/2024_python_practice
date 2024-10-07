class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state




n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
x = input()

roster = [None] * n

for i in range(n):
    x2 = Student(l[i][0], l[i][1], l[i][2], l[i][3])
    if x2.old == x:
        print(x2.name)
        break

