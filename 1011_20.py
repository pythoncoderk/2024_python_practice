h, w, n = map(int, input().split())
l1 = [list(input()) for _ in range(h)]
l2 = [list(map(int, input().split())) for _ in range(n)]

# print(l1)
# print(l2)

for i in range(n):
    print(l1[l2[i][0]][l2[i][1]])