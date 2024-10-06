class PersonalComputer:
    def __init__(self, ram, storage):
        self.__ram = ram
        self.storage = storage


pc = PersonalComputer(8, 128)
try:
    pc.ram += 8
    print(pc.ram)
except:
    print("プライベート変数にはアクセスできません。")
