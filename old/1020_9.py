a, w = map(int, input().split())
p_age = 15
p_kg = 60

class SkyDive:
    def __init__(self, age, kg):
        self.age = age
        self.kg = kg

    def ans(self):
        if p_age >= self.age and p_kg <= self.kg:
            return "Yes"
        return "No"


pai = SkyDive(a, w)
print(pai.ans())
