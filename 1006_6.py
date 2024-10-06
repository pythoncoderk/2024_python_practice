class PersonalComputer:
    ram = 64

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def ram_expansion(self, gb):
        self.ram += gb


pc = PersonalComputer(8, 128)
print(PersonalComputer.ram)
