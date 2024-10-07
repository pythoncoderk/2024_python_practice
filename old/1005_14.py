class Receipt(object):
    def __init__(self, day, price):
        self.day = day
        self.price = price


n = int(input())
total_points = 0
for i in range(n):
    x, y = map(int, input().split())
    receipt = Receipt(x, y)
    if "3" in str(receipt.day):
        ans_price = (receipt.price * 3) // 100
    elif "5" in str(receipt.day):
        ans_price = (receipt.price * 5) // 100
    else:
        ans_price = receipt.price // 100

    total_points += ans_price

print(total_points)
