n = int(input())
l = list(map(int, input().split()))

l_min = min(l)
for i, num in enumerate(l):
    if num == l_min:
        print(i + 1)
        break