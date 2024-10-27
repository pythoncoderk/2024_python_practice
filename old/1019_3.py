n = int(input())
l = list(map(int, input().split()))

x = int(input())

l2 = [l[i] for i in range(n) if l[i] >= x]

count = l2[0]
for i in l2:
    if count > i:
        count = i

print(count)