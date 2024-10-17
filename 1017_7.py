# coding: utf-8
# メソッドをオーバーライドしよう2

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)


class Hello(Greeting):
    def say_hello(self):
        print(self.msg + " " + self.target)
        print("YEAH YEAH YEAH!")


player = Hello()
player.say_hello()
