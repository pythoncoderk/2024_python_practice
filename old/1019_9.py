n = int(input())

l = [list(map(str, input().split())) for _ in range(n)]
k = int(input())

for i, j in l:
    if int(j) >= k:
        print(i)
