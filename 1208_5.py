l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    min_l = l[i]
    min_l_index = i
    for j in range(i, len(l)):
        if min_l > l[j]:
            min_l = l[j]
            min_l_index = j
    l[i], l[min_l_index] = l[min_l_index], l[i]

print(l)