# coding: utf-8
# クラスメソッドを呼び出そう

class Greeting:
    @classmethod
    def say_hello(cls):
        print("hello paiza")


# この下で、クラスメソッドを呼び出す
Greeting.say_hello()