n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    if l[i] % 2 == 0:
        print(i + 1)
        break