# coding: utf-8
# クラスにメソッドを定義しよう

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

class Hello(Greeting):
    # この下に、say_helloメソッドを記述する
    def say_hello(self):
        print(self.msg, self.target)

player = Hello()
player.say_hello()
