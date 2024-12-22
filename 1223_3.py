n, m = map(int, input().split())

l = list(map(str, input().split()))

l2 = [i for i in l if len(i) >= m]

print(*l2)
