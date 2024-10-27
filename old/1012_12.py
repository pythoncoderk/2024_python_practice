class Sea:
    def __init__(self, arr, hot=20):
        self.arr = arr
        self.hot = hot

    def lists(self):
        if min(self.arr) >= self.hot:
            return "OK"
        else:
            return "NG"


l = [int(input()) for _ in range(3)]
sea = Sea(l)
print(sea.lists())