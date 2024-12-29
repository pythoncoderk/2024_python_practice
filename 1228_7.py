from collections import deque

k = int(input())
s = list(input())
t = list(input())

if len(s) + 1 == len(t):
    s.append("ZZZ")
    s.sort()
    t.sort()
    for i in range(len(s)):
        
