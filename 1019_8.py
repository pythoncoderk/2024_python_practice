n = int(input())

l = [list(map(int, input().split())) for i in range(n)]

x_s, x_t = map(int, input().split())
y_s, y_t = map(int, input().split())

count = 0
for i in range(n):
    if x_s <= l[i][0] <= x_t and y_s <= l[i][1] <= y_t:
        count += 1

print(count)