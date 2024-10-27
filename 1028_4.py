l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    index_l = len(l) - 1
    for j in range(len(l) - 1, i, -1):
        if l[j - 1] > l[j]:
            l[j], l[j - 1] = l[j - 1], l[j]

print(l)


