# coding: utf-8
# 呼び出し元へ例外を伝えよう

import sys

def test_exception(number):
    try:
        return 100 / number

    except ZeroDivisionError as e:
        raise e
    finally:
        print("処理が終了しました")


try:
    test_exception(0)

except ZeroDivisionError as e:
    sys.stderr.write('0で割り算できません')
