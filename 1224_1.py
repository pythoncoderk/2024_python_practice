n = int(input())

if n <= 41: print("AGC" + str(n).zfill(3))
else: print("AGC" + str(n + 1).zfill(3))