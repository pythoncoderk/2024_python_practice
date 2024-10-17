# coding: utf-8
# 間違い探し

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    def say_hello(self, target):
        self.target = target
        print(self.msg, target)


player = Hello()
player.say_hello("python")
