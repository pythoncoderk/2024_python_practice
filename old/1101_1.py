n, m = map(int, input().split())
count_r = 0
count_l = 0
times = 3600
now = "r"
while times >= 1:
    if now == "r":
        times -= n
        count_r += 1
        now = "l"
    else:
        times -= m
        count_l += 1
        now = "r"

print(count_l)