class Test:
    def __init__(self, name, age, bir, state):
        self.name = name
        self.age = age
        self.bir = bir
        self.state = state

    def ans(self):
        print(self.name, self.age, self.bir, self.state)

n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])

l2 = sorted(l, key=lambda x: x[1])

for i in range(n):
    test = Test(l2[i][0], l2[i][1], l2[i][2], l2[i][3])
    test.ans()