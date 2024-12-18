n, d = map(int, input().split())
s = list(input())

flag = 0
for i in range(n):
    if s[i] == "@":
        s[i] = "."
        flag += 1

    if flag == d:
        print(s.count("."))
        exit()
