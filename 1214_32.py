n, r = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

# print(n, r)
# print(l)

for i in range(n):
    if l[i][0] == 1:
        if 1600 <= r <= 2799:
            r += l[i][1]
    else:
        if 1200 <= r <= 2399:
            r += l[i][1]
print(r)