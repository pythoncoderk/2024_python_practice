from decimal import Decimal, ROUND_HALF_UP

n, m = map(int, input().split())
for i in range(m):
    x = int(input())
    x /= n
    x = Decimal(str(x)).quantize(Decimal("0"), ROUND_HALF_UP)
    x *= n
    print(n if x == 0 else x)
