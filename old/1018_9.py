print(1)
try:
    number = 0
    answer = 100 / number
    print(answer2)
except ZeroDivisionError as e:
    print("0では割り算できません")
    print(e)
finally:
    print(2)