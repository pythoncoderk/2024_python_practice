l = [7, 2, 9, 5, 1, 8, 4, 10, 6, 3]

for i in range(len(l)):
    for j in range(i, 0, -1):
        if l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]

print(l)


