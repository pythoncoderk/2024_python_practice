import itertools

n = int(input())
l = list(map(int, input().split()))
all_p = []
l_s = set(l)

for j in range(n):
    all_f = []
    for i in itertools.combinations(l, j):
        all_f.append(sum(i))
        ans_x = sum(l) - sum(i)
        all_f.append(ans_x)
        all_f.append(abs(all_f[0] - all_f[1]))
        all_p.append(all_f)

        all_f = []
all_p = sorted(all_p, key=lambda x: x[2])
# print(all_p)
print(all_p[0][0] if all_p[0][0] > all_p[0][1] else all_p[0][1])