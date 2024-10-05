class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def ram_expansion(self, gb):
        self.ram += gb


pc = PersonalComputer(8, 128)
pc.ram_expansion(16)


print(pc.ram)
