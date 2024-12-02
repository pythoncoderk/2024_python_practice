s = input()

count = []
for i in range(len(s)):
    count.append(s.count(s[i]))

print("Yes" if max(count) == 2 and min(count) == 2 else "No")