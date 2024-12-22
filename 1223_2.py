n, m = map(int, input().split())

l = [list(map(int, input().split())) for i in range(2)]

count = 0
for i in range(n):
    for j in range(n):
        if l[0][i] + l[1][j] == m:
            count += 1

print(count)