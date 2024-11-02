import bisect

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]

# print(l)
# print(l2)

for i in range(m):
    x = l2[i][0] - 1
    y = l2[i][1]
    x_1 = l[x][0]
    y_2 = l[x][1]
    xxx = (x_1 * y_2) + 1
    print(xxx)
