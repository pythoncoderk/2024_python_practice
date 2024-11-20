class Car:
    def __init__(self, km, l):
        self.km = km
        self.l = l

    def ans(self):
        return self.km // self.l

km = int(input())
l = int(input())
car = Car(km, l)
print(car.ans())