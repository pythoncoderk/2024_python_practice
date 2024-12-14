s = input()

matu = []
hatena = []
batsu = []
ans_count = 0
for i in range(len(s)):
    if s[i] == "o":
        matu.append(str(i))
    elif s[i] == "?":
        hatena.append(str(i))
    else:
        batsu.append(str(i))
for i in range(0, 10000):
    x = str(i).zfill(4)
    # x = ("0123")
    count = 0
    flag = True
    for j in matu:
        if j not in x:
            flag = False
    for q in batsu:
        if q in x:
            flag = False
    if flag:
        ans_count += 1

print(ans_count)




