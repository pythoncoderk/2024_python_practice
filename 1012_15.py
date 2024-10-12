n = int(input())
l = list(input())

count = 0
for i in range(n - 2):
    if l[i] == "#" and l[i + 1] == "." and l[i + 2] == "#":
        count += 1

print(count)