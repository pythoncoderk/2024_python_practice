class Monster():
    def __init__(self, total, gets):
        self.total = total
        self.gets = gets


n = int(input())
m = int(input())

sample = Monster(n, m)
print(sample.total - sample.gets)

