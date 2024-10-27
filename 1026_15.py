import bisect

n, x = map(int, input().split())
l = list(map(int, input().split()))

print(bisect.bisect(l, x))