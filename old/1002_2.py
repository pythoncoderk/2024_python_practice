def kaijyo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * kaijyo(n - 1)

print(kaijyo(10))