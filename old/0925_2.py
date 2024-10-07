n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
x = input()
for i in range(n):
    if l[i][1] == x:
        print(l[i][0])

