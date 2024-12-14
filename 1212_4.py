import math

n = int(input())
l = list(map(int, input().split()))

print(math.ceil((sum(l) / n)))