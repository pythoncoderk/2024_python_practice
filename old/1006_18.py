class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Laptop(PersonalComputer):
    def __init__(self, ram, storage, key_layout):
        super().__init__(ram, storage)
        self.key_layout = key_layout


class PaizaBook(Laptop):
    pass


# 以下にコードを記述
print(PaizaBook.__mro__)
