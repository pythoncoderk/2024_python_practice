l = [2, 5, 1, 4, 6, 3]


for i in range(len(l)):
    now_int = l[i]
    for j in range(i, -1, -1):
        if now_int < l[j]:
            l[j + 1], l[j] = l[j], l[j + 1]

print(l)


