l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    min_l = l[i]
    min_index = i
    for j in range(i, len(l)):
        if l[j] < min_l:
            min_l = l[j]
            min_index = j
    l[i], l[min_index] = l[min_index], l[i]

print(l)