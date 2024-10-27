n = int(input())
l = [list(map(str, input().split())) for _ in range(n)]
k = int(input())

class Member:
    def __init__(self, name, age, birth, add):
        self.name = name
        self.age = age
        self.birth = birth
        self.add = add

for i in l:
    a, b, c, d = i
    if int(b) == k:
        print(a)

