class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Laptop(PersonalComputer):
    # 以下にコードを記述
    def __init__(self, ram, strage, key_layout):
        super().__init__(ram, strage)
        self.key_layout = key_layout


laptop_pc = Laptop(8, 128, "jis")
print(laptop_pc.key_layout)
