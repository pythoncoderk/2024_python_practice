s = input()

ans = ""
i = 0

count = 0
while s != "":
    if len(s) >= 2:

        if s[0] == "0" and s[1] == "0":
            s = s[2:]
            count += 1
        else:
            s = s[1:]
            count += 1
    else:
        s = s[1:]
        count += 1

print(count)