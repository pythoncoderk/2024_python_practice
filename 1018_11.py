print(1)
try:
    number = 0
    answer = 100 / number
    print(answer2)

except NameError as e:
    print("未定義")
except Exception as e:
    print("予期せぬエラー")
    print(e)
finally:
    print(2)
