s = input()
total = 0
now = ""
for i in s:
    if i == "+" or i == "-":
        now = i
    else:
        if now == "+":
            total += int(i)
        elif now == "":
            total = int(i)
        else:
            total -= int(i)

print(total)