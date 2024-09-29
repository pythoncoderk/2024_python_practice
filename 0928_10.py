l = [list(map(str, input())) for i in range(12)]

count = 0
for i in range(len(l)):
    x = len(l[i])
    if i + 1 == x:
        count += 1


print(count)