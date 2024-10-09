# coding: utf-8
# クラスにインスタンス変数を追加しよう

class Greeting:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print("hello " + self.name)


paiza = Greeting("paiza")
paiza.say_hello()
