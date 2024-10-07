s = list(input())
#
# print(s)
l = []
for i in range(len(s)):
    if s[i] != ".":
        l.append(s[i])

print("".join(l))