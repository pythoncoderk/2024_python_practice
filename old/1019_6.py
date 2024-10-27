n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
k = int(input())
x_n = l[-1][0]
y_n = l[-1][1]

count = 0
for i in range(n):
    x, y = l[i][0], l[i][1]
    m = abs(x - x_n) + abs(y - y_n)
    if m <= k:
        count += 1

print(count)