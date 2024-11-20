n, k = map(int, input().split())
count = 0
flag = True
while n > 0:

    for i in range(k):
        if n > 0:
            n -= 1
        else:
            flag = False
            break
    if flag:
        count += 1

print(count - 1)