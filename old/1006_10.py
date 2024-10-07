class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_age(self, year):
        self.age += year

class Programmer(Person):
    pass

kirishima = Programmer("kiri", 15)
print(kirishima.name, kirishima.age)