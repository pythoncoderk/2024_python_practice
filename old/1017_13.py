# coding: utf-8
# 親クラスのメソッドを呼び出す

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    def say_hello(self):

        print("YEAH YEAH YEAH!")

test = Greeting()
test.say_hello()
player = Hello()
player.say_hello()
