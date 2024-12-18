import itertools

n, m = map(int, input().split())
l = list(map(int, input().split()))

if min(l) > m:
    print("No")
    exit()

ans = []
for i in range(2, n + 1):
    for pair in itertools.combinations(l, i):
        ans.append(sum(pair))

for i in range(len(ans)):
    if m % ans[i] != 0:
        print("Yes")
        exit()

print("No")