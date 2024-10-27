# coding: utf-8
# クラスからオブジェクトを作成しよう

class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("hello " + self.name)

# この下に、必要な処理を記述します

greeting1 = Greeting("paiza")
greeting1.say_hello()