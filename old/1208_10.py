def fib_memo(n):
    memo = [None] * (n + 1)

    def _fib(n):
        if n == 0 or n == 1:
            return 1
        if memo[n] != None:
            return memo[n]
        memo[n] = _fib(n - 1) + _fib(n - 2)
        return memo[n]
    return _fib(n)

for i in range(35):
    print(fib_memo(i))