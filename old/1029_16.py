l1 = [1, 3, 5, 7, 8, 10, 12]
l2 = [4, 6, 9, 11]
l3 = [2]

x, y = map(int, input().split())
xy_list = [x, y]
def chk(a, arr_01, arr_02, arr_03):
    if a in arr_01:
        return 1
    elif a in arr_02:
        return 2
    else:
        return 3

ans = []
for i in xy_list:
    ans.append(chk(i, l1, l2, l3))

print("Yes" if ans[0] == ans[1] else "No")