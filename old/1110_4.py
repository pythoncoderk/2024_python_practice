class Music:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        return abs(self.a - self.b)

a, b = map(int, input().split())
music = Music(a, b)
print(music.ans())