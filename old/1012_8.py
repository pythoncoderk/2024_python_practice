class Bread:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name + "pan"


n = input()
bread = Bread(n)
print(bread.get_name())