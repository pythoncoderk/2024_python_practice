s = input()

class Change:
    def __init__(self, s):
        self.s = s

    def loops(self, x):
        ans = ""
        for i in range(x):
            if i % 2 == 0:
                ans += self.s[i]
        return ans


change = Change(s)
print(change.loops(len(s)))