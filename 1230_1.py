l = list(map(int, input().split()))

l2 = ["F", "M", "T"]

i = 0
while True:
    i += 1
    l[0] -= l[i]
    if l[0] < 0:
        print(l2[i - 1])
        break

    if i >= 3:
        i = 0
