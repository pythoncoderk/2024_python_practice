n, m = map(int, input().split())
p = int(input())
l = list(map(int, input().split()))
l2 = [l[i] for i in range(len(l)) if l[i] % n == 0]

for i in range(m):
    x = int(input())
    diff = abs(x - l2[0])
    diff_num = l2[0]
    for j in range(len(l2)):
        if abs(x - l2[j]) <= diff:
            diff = abs(x - l2[j])
            diff_num = l2[j]
    print(diff_num)
