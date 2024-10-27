n, k = map(int, input().split())
l1 = [list(map(str, input().split())) for _ in range(n)]
l2 = [list(map(str, input().split())) for _ in range(k)]

def changeName(num, name, arr):
    target = int(num) - 1
    arr[target][0] = l2[i][1]
    return arr

for i in range(k):
    changeName(l2[i][0], l2[i][1], l1)

for i in l1:
    print(*i)