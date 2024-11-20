class Check:
    def __init__(self, arr):
        self.arr = arr

    def ans(self):
        list(self.arr).sort()
        return self.arr[1]

l = list(map(int, input().split()))
l.sort()
chk = Check(l)
print(chk.ans())