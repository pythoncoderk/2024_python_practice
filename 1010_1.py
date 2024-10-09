
class Player:

    def walk(self):
        print("勇者は歩く")

    def attack(self, enemy):
        print("勇者は" + enemy + "を攻撃した！")


player1 = Player()
player1.walk()
player1.attack("スライム")