def fibo(x):
    if x == 0 or x == 1:
        return 1
    return fibo(x - 1) + fibo(x - 2)


for i in range(35):
    print(fibo(i))