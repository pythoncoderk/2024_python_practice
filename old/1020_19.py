class Chk:
    def __init__(self, string):
        self.string = string

    def last_word(self):
        if self.string[-1] == "d":
            return "Yes"
        return "No"
s = input()
chk = Chk(s)
print(chk.last_word())