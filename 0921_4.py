n = int(input())

count = 0
while True:
    x = list(str(count))
    for i in range(len(x)):
        x[i] = int(x[i])
    total = 0
    for j in range(len(x)):
        total += 3 ** x[j]
    if total == n:
        break
    else:
        count += 1

print(len(x))
print(*x)