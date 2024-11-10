n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(2)]

l2 = []

for i in range(m):
    l2.append([l[0][i], l[1][i]])


print(l2)
count_ans = 0
xx = 0
for i in range(m-1):
    if l2[i][0] == 1:
        break
    x = l2[i + 1][0] - l2[i][0]
    count_ans += x
    elif x >= l2[i][1]:
        xx = l2[i + 1][0] - l2[i][0] - l2[i][1]
        l2[i + 1][1] += xx

final = l2[-1]
yy = n - final[0] + 1
if final[1] == yy:
    count_ans += n - final[0]
else:
    print(-1)
    exit()

print(count_ans)

