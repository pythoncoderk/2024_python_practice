s = input()

count = 0
l = []
rain = True
for i in range(len(s)):
    if s[i] == "R":
        rain = False
    else:
        rain = True
        count = 0

    if not rain:
        count += 1
        l.append(count)

if l == []:
    print(0)
else:
    print(max(l))