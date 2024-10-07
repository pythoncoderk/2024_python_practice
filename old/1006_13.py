class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def ram_expansion(self, gb):
        self.ram += gb
        print(self.ram)


class Laptop(PersonalComputer):
    pass


laptop_pc = Laptop(8, 128)
# 以下にコードを記述
laptop_pc.ram_expansion(8)
