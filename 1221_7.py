l = list(map(str, input().split()))

name = []
count = []

for i in range(len(l)):
    if l[i] not in name:
        name.append(l[i])
        count.append(1)
    else:
        x = name.index(l[i])
        count[x] += 1

for _ in name:
    print(_)

for _ in count:
    print(_)
