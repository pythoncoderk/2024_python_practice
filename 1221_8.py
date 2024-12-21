l = list(map(str, input().split()))

d = {}

for i in range(len(l)):
    if l[i] not in d:
        d[l[i]] = 1
    else:
        d[l[i]] += 1

d_key = list(d.keys())
d_value = list(d.values())

for i in range(len(d_key)):
    print(d_key[i], d_value[i])

