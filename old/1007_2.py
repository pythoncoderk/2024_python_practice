# 九九の表を作成してみよう

def multiply(x, y):
    return x * y

for num in range(1, 10):
    for j in range(1, 10):
        if j != 9:
            print(multiply(num, j), end=", ")
        else:
            print(multiply(num, j))
