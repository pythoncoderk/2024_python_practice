n = int(input())
l1 = list(map(int, input().split()))
l1.sort()
q = int(input())
l2 = [int(input()) for i in range(q)]

l3 = l1[::]
def d_s(x, arr):
    len_arr = len(arr) // 2
    arr_l = arr[:len_arr]
    arr_r = arr[len_arr:]
    

for i in range(q):
    d_s(l2[i], l3)
