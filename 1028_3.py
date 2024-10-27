l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    index_l = i
    for j in range(i, -1, -1):
        if l[index_l] < l[j]:
            l[index_l], l[j] = l[j], l[index_l]
            index_l = j
print(l)