class Word:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        print(self.b, self.a)

a, b = map(str, input().split())
word = Word(a, b)
word.ans()