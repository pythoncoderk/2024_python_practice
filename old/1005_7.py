class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    # 以下にコードを記述
    def ram_expansion(self, ram_2):
        self.ram += ram_2

pc = PersonalComputer(8, 128)
pc.ram_expansion(8)
print(pc.ram)
