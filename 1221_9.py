n = input()
m = int(input())

for i in range(m):
    num = input()
    if n == num:
        print("first")
    elif str(int(num) + 1) == n or str(int(num) - 1) == n:
        print("adjacent")
    elif n[-4:] == num[-4:]:
        print("second")
    elif n[-3:] == num[-3:]:
        print("third")
    else:
        print("blank")