import re

n = int(input())

for i in range(n):
    x = input()
    x2 = re.fullmatch(r"(\d{1}|\d{2}|\d{3})\.(\d{1}|\d{2}|\d{3})\.(\d{1}|\d{2}|\d{3})\.(\d{1}|\d{2}|\d{3})", x)
    print(False if x2 is None else True)