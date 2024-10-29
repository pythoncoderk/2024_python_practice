import bisect

n = int(input())
l1 = list(map(int, input().split()))
q = int(input())
l2 = [int(input()) for i in range(q)]
l1.sort()

for i in range(q):
    print(bisect.bisect_left(l1, l2[i]))