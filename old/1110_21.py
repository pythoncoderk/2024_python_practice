def fib(n):
    memo = [None] * n
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo

for i in fib(35):
    print(i)

