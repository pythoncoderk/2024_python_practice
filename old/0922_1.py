n, m = map(int, input().split())
p = int(input())
l = list(map(int, input().split()))
l2 = [l[i] for i in range(p) if l[i] % n == 0]

for i in range(m):
    x = int(input())
    l_min = abs(l2[0] - x)
    min_num = l2[0]
    for j in range(len(l2)):
        if abs(l2[j] - x) < l_min:
            l_min = abs(l2[j] - x)
            min_num = l2[j]
            print(min_num)
        else:
            if j == len(l2) - 1:
                print(min_num)
