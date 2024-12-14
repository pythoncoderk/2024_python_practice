a, b, c, d, e = map(int, input().split())

l = [["A", a], ["B", b], ["C", c], ["D", d], ["E", e]]
ans = [["A", a], ["B", b], ["C", c], ["D", d], ["E", e]]
# print(l)

for i in range(len(l)):
    for j in range(len(l)):
        if l[i][0] != l[j][0]:
            x = [l[i][0] + l[j][0], l[i][1] + l[j][1]]
            ans.append(x)

for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            xx = [l[i][0], l[j][0], l[k][0]]
            if max(xx.count(l[i][0]), xx.count(l[j][0]), xx.count(l[k][0])) == 1:
                x = [l[i][0] + l[j][0] + l[k][0], l[i][1] + l[j][1] + l[k][1]]
                ans.append(x)

for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            for aa in range(len(l)):
                xx = [l[i][0], l[j][0], l[k][0], l[aa][0]]
                if max(xx.count(l[i][0]), xx.count(l[j][0]), xx.count(l[k][0]), xx.count(l[aa][0])) == 1:
                    x = [l[i][0] + l[j][0] + l[k][0] + l[aa][0], l[i][1] + l[j][1] + l[k][1] + l[aa][1]]
                    ans.append(x)

for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            for aa in range(len(l)):
                for bb in range(len(l)):
                    xx = [l[i][0], l[j][0], l[k][0], l[aa][0], l[bb][0]]
                    if max(xx.count(l[i][0]), xx.count(l[j][0]), xx.count(l[k][0]), xx.count(l[aa][0]), xx.count(l[bb][0])) == 1:
                        x = [l[i][0] + l[j][0] + l[k][0] + l[aa][0] + l[bb][0], l[i][1] + l[j][1] + l[k][1] + l[aa][1] + l[bb][1]]
                        ans.append(x)


# print(len(ans))
for i in range(len(ans)):
    ans[i][0] = list(ans[i][0])
    ans[i][0].sort()
    ans[i][0] = "".join(ans[i][0])

# print(ans)

l_check = []
final = []
for i in range(len(ans)):
    if ans[i][0] not in l_check:
        l_check.append(ans[i][0])
        final.append([ans[i][0], ans[i][1]])
# print(final)

f = sorted(final, key=lambda x: x[0])
f = sorted(f, key=lambda x: x[1], reverse=True)
# print(f)

for i in range(len(f)):
    print(f[i][0])