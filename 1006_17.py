class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Laptop(PersonalComputer):
    def __init__(self, ram, storage, key_layout):
        super().__init__(ram, storage)
        self.key_layout = key_layout


# 以下にコードを記述
class PaizaBook(Laptop):
    pass


paizabook = PaizaBook(8, 128, "jis")
print(paizabook.ram, paizabook.storage, paizabook.key_layout)
