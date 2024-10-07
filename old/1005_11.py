a, b, r = map(int, input().split())
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    ans = (x - a) ** 2 + (y - b) ** 2
    print("silent" if ans >= r ** 2 else "noisy")
