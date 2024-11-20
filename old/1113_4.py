class Str:
    def __init__(self, s):
        self.s = s

    def ans(self):
        if len(self.s) <= 20:
            return "OK"
        return "NG"

s = input()
st = Str(s)
print(st.ans())