class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Laptop(PersonalComputer):
    pass


laptop_pc = Laptop(8, 128)
# 以下にコードを記述
print(laptop_pc.storage)