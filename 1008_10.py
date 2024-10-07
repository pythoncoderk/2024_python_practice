class MyClass:
    def __init__(self):
        self.name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

a = MyClass()
a.setName("tama")
print(a.getName())
