class Age:
    def __init__(self, age):
        self.age = age

    def ans(self):
        return self.age - 5

n = int(input())

age = Age(n)
print(age.ans())