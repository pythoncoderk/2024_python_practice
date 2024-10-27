def test(number):
    print(2)
    ans = 100 / number
    return ans

print(1)

try:
    ans = test(0)
    print(3)
except ZeroDivisionError as e:
    print(4)
    print(e)