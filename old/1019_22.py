n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l1.sort(reverse=True)
l2.sort(reverse=True)

l1 = set(l1)
l2 = set(l2)

# print(l1)
# print(l2)

for i in range(len(l2)):
    for j in range(len(l1)):
        if l2[i] >= l1[j] and l1[j] != 9999999999999999999999999:
            l1[j] = 9999999999999999999999999
            break

ans = len(l1) - l1.count(9999999999999999999999999)
set_ans = set(l1)

print(sorted(set_ans)[0] if ans == 1 else -1)