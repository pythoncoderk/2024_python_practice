class Page:
    def __init__(self, page):
        self.page = page

    def ans(self):
        return self.page * 100
n = int(input())
page = Page(n)
print(page.ans())