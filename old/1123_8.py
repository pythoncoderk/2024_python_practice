class Words:
    def __init__(self, s, l):
        self.s = s
        self.l = l
    def ans(self):
        x = ""
        for i in self.s:
            if i not in self.l:
                x += i
        return x

l = ["a", "e", "i", "o", "u"]
s = input()
word = Words(s, l)
print(word.ans())
