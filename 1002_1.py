def rec_sum(n):
    print(n)
    if n == 0:
        return 0
    return n + rec_sum(n - 1)


rec_sum(10)