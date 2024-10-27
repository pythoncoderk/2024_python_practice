print(1)

try:
    number = 0
    raise Exception("テスト")
    print(answer)
except Exception as e:
    print("予期せぬ")
    print(e)
finally:
    print(4)