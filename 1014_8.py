class Book:
    def __init__(self, n, a):
        self.n = n
        self.a = a

    def ans(self):
        x = self.n // self.a
        y = self.n % self.a
        if self.n < self.a:
            return 1
        else:
            if y != 0:
                return x + 1
            return x

n = int(input())
a = int(input())
book = Book(n, a)
print(book.ans())