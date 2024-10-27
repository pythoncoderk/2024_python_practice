class Enemy:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(self.name + "は勇者を攻撃した！")

enemies = []

enemies.append(Enemy("スライム"))
enemies.append(Enemy("モンスター"))
enemies.append(Enemy("ドラゴン"))

for enemy in enemies:
    enemy.attack()