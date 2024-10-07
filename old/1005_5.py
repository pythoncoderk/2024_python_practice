class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


pc = PersonalComputer(8, 128)
print(pc.ram)