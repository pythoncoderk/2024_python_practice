class Book:
    def __init__(self, page):
        self.page = page

    def ans(self):
        return self.page * 100

n = int(input())
book = Book(n)
print(book.ans())