n = int(input())
l = [list(map(str, input().split())) for _ in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])

l = sorted(l, key=lambda x: x[1])

class User:
    def __init__(self, name, age, birth, add):
        self.name = name
        self.age = age
        self.birth = birth
        self.add = add

for i in l:
    a, b, c, d = i
    print(a, b, c, d)