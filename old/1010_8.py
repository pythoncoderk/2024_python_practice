# coding: utf-8
# 間違い探し

class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("hello " + self.name)

paiza = Greeting("paiza")
paiza.say_hello()
