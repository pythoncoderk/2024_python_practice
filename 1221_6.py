l = list(map(str, input().split()))
name = input()
for i in range(len(l)):
    if l[i] == name:
        print(i)
        exit()
        