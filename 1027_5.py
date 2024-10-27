class Total:
    def __init__(self, tall):
        self.a = tall
    
    def ans(self):
        return self.a + 170

n = int(input())
a_kun = Total(n)
print(a_kun.ans())