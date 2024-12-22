n = int(input())
l = list(map(int, input().split()))

average = sum(l) // n

# print(average)

for i in l:
    print(abs(average - i))