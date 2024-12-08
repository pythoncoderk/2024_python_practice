class Test:
    def __init__(self, name, age, bir, fr):
        self.name = name
        self.age = age
        self.bir = bir
        self.fr = fr

    def ans(self):
        return self.name

n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = input()

for i in range(n):
    if l[i][1] == m:
        test = Test(l[i][0], l[i][1], l[i][2], l[i][3])
        print(test.ans())