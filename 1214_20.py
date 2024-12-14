a, b = map(int, input().split())
c, d = map(int, input().split())

x = []
y = []
for i in range(a, b + 1):
    x.append(i)

for i in range(c, d + 1):
    y.append(i)

# print(x)
# print(y)

ans = []
for i in range(len(x)):
    for j in range(len(y)):
        ans.append(x[i] - y[j])

print(max(ans))