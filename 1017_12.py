# coding: utf-8
# クラスの中のメソッドを呼び出す

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)


    def say_yeah(self):
        print("YEAH YEAH YEAH!")


player = Greeting()
player.say_hello()

test = Greeting()
test.say_yeah()