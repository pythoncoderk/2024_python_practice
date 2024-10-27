n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
k = int(input())

count = 0
x_n, y_n = l[-1]
for x, y in l:
    if abs(x_n - x) + abs(y_n - y) <= k:
        count += 1

print(count)

