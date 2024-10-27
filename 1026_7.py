n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
l2 = l[::]
l3 = [i for i in range(n)]

while len(l2) >= 2:
    half = len(l2) // 2
    chk_l01 = l2[:half]
    chk_l301 = l3[:half]
    chk_l02 = l2[half:]
    chk_l302 = l3[half:]
    if m in chk_l01:
        l2 = chk_l01
        l3 = chk_l301
    else:
        l2 = chk_l02
        l3 = chk_l302

print(l3[0] + 1)