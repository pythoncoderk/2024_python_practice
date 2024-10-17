# coding: utf-8
# クラスを継承しよう

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

# この下に、Greetingクラスを継承した、Helloクラスを定義する。
# そこに、say_hello()メソッドの定義を記述する。

class Hello(Greeting):
    def say_hello(self):
        print(self.msg, self.target)


player = Hello()
player.say_hello()
