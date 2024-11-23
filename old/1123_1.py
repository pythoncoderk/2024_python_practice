n, k = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
flag = True
for i in range(k):
    for j in range(k):
        if l2[i] in l1:
            print(i + 1)
            flag = False
            break

if flag:
    print(-1)