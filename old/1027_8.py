class School:
    def __init__(self, students):
        self.students = students

    def ans(self):
        return self.students // 2

n = int(input())
sample = School(n)
print(sample.ans())