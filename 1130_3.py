import numpy as np

n, m = map(int, input().split())
l1 = np.array(list(map(int, input().split())))
l2 = np.array(list(map(int, input().split())))

# print(l1)
# print(l2)

for i in range(m):
    x = l2[i] >= l1
    y = np.where(x == True)
    if len(y[0]) == 0:
        print(-1)
    else:
        print(np.amin(y[0]) + 1)