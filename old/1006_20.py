try:
    a = float(input())
    b = float(input())
    print(a / b)
except ValueError:
    print("入力値は数字でなければなりません。")
except ZeroDivisionError:
    print("0 で割る事はできませ～ん！")

