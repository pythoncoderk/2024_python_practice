class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_age(self, year):
        self.age += year


kirishima = Person("Kirishima", 15)
print(kirishima.add_age(15))
