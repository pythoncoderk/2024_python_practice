# import lesson_pakege.utels
# from lesson_pakege.talk import human
# from lesson_pakege.talk import amimal
# from lesson_pakege.talk import *
#
# print(amimal.sing())
# print(amimal.cry())
#
# r = lesson_pakege.utels.say_twice("hello")
# print(r)
#
# print(human.sing())
# print(human.cry())
try:
    from lesson_pakege import utels
except ImportError:
    from lesson_pakege.tools import utels
utels.say_twice("word")
