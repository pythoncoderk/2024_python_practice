l = list(map(int, input().split()))

l.sort()
count = 0
while True:
    if len(l) <= 1:
        break
    elif l[0] == l[1]:
        l.pop(0)
        l.pop(0)
        count += 1
    else:
        l.pop(0)

print(count)