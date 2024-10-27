import bisect
a = [2, 3, 5, 7, 11, 13, 17, 19]
print(bisect.bisect_left(a, 11))
print(bisect.bisect_right(a, 11))
print(bisect.bisect(a, 11))