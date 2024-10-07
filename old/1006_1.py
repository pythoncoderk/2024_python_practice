n = int(input())
l = list(map(int, input().split()))
sum_l = sum(l)
x = 0
ans_l = []
flag_l = 0

while flag_l < n:
    count = bin(x)[2:]
    count_2 = count.zfill(n)
    count_l = list(count_2)
    count_l = [int(count_l[i]) for i in range(n)]
    flag_l = sum(count_l)
    total = 0
    sub_l = []
    for i in range(n):
        if count_l[i] == 1:
            total += l[i]
    sub_l.append(total)
    sub_l.append(sum_l - total)
    sub_l.append(abs(sub_l[0] - sub_l[1]))
    ans_l.append(sub_l)
    x += 1

ans_l = sorted(ans_l, key=lambda x: x[2])
print(ans_l[0][1] if ans_l[0][0] < ans_l[0][1] else ans_l[0][0])

