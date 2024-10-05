n = input()
m = int(input())
flag = False
for i in range(m):
    x = input()
    if n not in x:
        print(x)
        flag = True

if flag is False:
    print("none")