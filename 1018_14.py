# coding: utf-8
# 間違い探し

import sys

print("Hello World")

try:
    raise ZeroDivisionError("強制エラー")
except ZeroDivisionError as e:
    sys.stderr.write("0では割り算はできません")


finally:
    print("Hello Python3")
