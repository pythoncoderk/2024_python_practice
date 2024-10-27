n = int(input())
l = [list(map(str, input().split())) for _ in range(n)]
x, y = map(int, input().split())

for i, j in l:
    if x <= int(j) <= y:
        print(i)
        