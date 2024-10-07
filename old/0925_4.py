class Human:
    """人間クラス"""

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def talk(self):
        print(f"こんにちは{self.name}です！")

    def walk(self):
        print(f"{self.name}は歩きます！")

ikuma = Human("ikuma", 170, 60)
print(ikuma.name, ikuma.height, ikuma.weight)
ikuma.talk()
ikuma.walk()

sato = Human("sato", 160, 50)
print(sato.name, sato.height, sato.weight)
sato.talk()
sato.walk()