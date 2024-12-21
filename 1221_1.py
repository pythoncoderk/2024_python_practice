from collections import deque

n = int(input())

l = deque()

for i in range(n):
    name = input()
    if name not in l:
        l.appendleft(name)
    else:
        name_index = l.index(name)
        l.remove(name)
        l.appendleft(name)

for _ in l:
    print(_)


