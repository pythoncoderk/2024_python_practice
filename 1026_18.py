import re
l = [input() for i in range(8)]
l_x = l[::]
count = 0
for i in range(8):
    if "#" in l[i]:
        l[i] = l[i].replace(".", "*")

l3 = []
for i in range(8):
    ans = ""
    for j in range(8):
        ans += l[j][i]
    l3.append(ans)

for i in range(8):
    if "#" in l3[i]:
        l3[i] = l3[i].replace(".", "!")


count = 0
for i in range(8):
    count += l3[i].count(".")

print(count)


