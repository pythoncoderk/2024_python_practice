class PersonalComputer:
    type = "classic computer"

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def ram_expansion(self, gb):
        self.ram += gb


k = PersonalComputer(5, 6)
print(k.type)
