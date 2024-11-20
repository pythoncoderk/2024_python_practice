l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    min_l = l[i]
    index_l = i
    for j in range(i, len(l)):
        if l[j] < min_l:
            l[j], l[i] = l[i], l[j]
            min_l = l[i]
            index_l = i

print(l)


