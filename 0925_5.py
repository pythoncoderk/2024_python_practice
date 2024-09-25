class Human:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self._height_meter = self._calc_meter()
        self._age = 0

    def talk(self):
        print(f"こんにちは！{self.name}です！")
    def walk(self):
        print(f"{self.name}は歩きます！")

    def _calc_meter(self):
        return self.height / 100

    @property
    def bmi(self):
        return self.weight / self._height_meter ** 2

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        try:
            value = int(value)
        except ValueError("ageは整数で指定してください！")
        if value < 0:
            raise ValueError("ageは整数で指定してください。")
        self._age = value


ikuma = Human("ikuma", 170, 60)
print(ikuma.name, ikuma.height, ikuma.weight)
ikuma.talk()
ikuma.walk()
print(ikuma.bmi)
ikuma.age = 20
print(ikuma.age)

sato = Human("sato", 160, 50)
print(sato.name, sato.height, sato.weight)
sato.talk()
sato.walk()
print(sato.bmi)

