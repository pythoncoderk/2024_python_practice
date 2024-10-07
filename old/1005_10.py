from decimal import *

n, m, k = map(int, input().split())
a_l = list(map(float, input().split()))

l = [list(map(int, input().split())) for i in range(m)]
l3 = []
for i in range(m):
    l2 = []
    total = 0
    for j in range(n):
        x = l[i][j] * a_l[j]
        total += x
    total = Decimal(str(total))
    l3.append(total.quantize(Decimal("0"), rounding=ROUND_HALF_UP))
l3.sort(reverse=True)

for i in range(k):
    print(l3[i])