class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_age(self, year):
        self.age += year

    def add_age_print_age(self, year):
        self.add_age(year)
        print(self.age)

kirishima = Person("kirishima", 15)
kirishima.add_age_print_age(4)