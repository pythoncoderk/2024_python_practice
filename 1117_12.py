class St:
    def __init__(self, s):
        self.s = s

    def ans(self):
        for i in self.s:
            print(i)

s = input()
st = St(s)
st.ans()
