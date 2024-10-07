class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

# 以下にコードを記述

class Laptop(PersonalComputer):
    pass


laptop_pc = Laptop(8, 128)
print(laptop_pc.ram)
