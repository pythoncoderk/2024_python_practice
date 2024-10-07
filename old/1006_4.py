class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def ram_expansion(self, gb):
        self.ram += gb

    def storage_expansion(self, gb):
        self.storage += gb

    def ram_and_storage_expansion(self, ram_gb, storage_gb):
        self.ram_expansion(ram_gb)
        self.storage_expansion(storage_gb)

pc = PersonalComputer(8, 128)
pc.ram_and_storage_expansion(8, 128)
print(pc.ram, pc.storage)
