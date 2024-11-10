class Message:
    def __init__(self, st):
        self.st = st

    def ans(self):
        return self.st + "!"

s = input()
me = Message(s)
print(me.ans())