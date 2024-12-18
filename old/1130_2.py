n, d = map(int, input().split())
s = list(input())

flag = 0
for i in range(n - 1, -1, -1):
    if s[i] == "@":
        s[i] = "."
        flag += 1
    if flag == d:
        print("".join(s))
        exit()