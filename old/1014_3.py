class Chk:
    def __init__(self, st):
        self.st = st
        
    def count_str(self):
        if len(self.st) <= 10:
            return 0
        return len(self.st) - 10

s = input()

chk = Chk(s)
print(chk.count_str())