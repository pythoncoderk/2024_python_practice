class Book:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        return 500 - self.a - self.b

a = int(input())
b = int(input())
book = Book(a, b)
print(book.ans())