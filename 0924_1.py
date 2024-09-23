n, m = map(int, input().split())
w = int(input())

x = 0
while True:
    if x + n <= 1500:
        x += n
    else:
        break
    print(x, abs(x - w))
