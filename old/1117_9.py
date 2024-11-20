x = 256

while x != 1:
    x /= 2
    if x == 1:
        print("OK")
        break
    if x % 2 != 0:
        print("NG")
        break

# 出力結果 OK

