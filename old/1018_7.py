import sys
import traceback

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print("0では割り算できません！")
    # print(traceback.format_exc())
    sys.stderr.write(traceback.format_exc())
finally:
    print(2)