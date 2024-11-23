s = input()

flag = True
if len(s) % 2 != 0:
    flag = False

x = len(s) // 2
for i in range(len(s) // 2):
    if s[(2 * i + 1) - 1] != s[2 * i + 1]:
        flag = False
for j in range(len(s)):
    if s.count(s[j]) != 2:
        flag = False

print("Yes" if flag else "No")
