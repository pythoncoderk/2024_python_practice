v, t, s, d = map(int, input().split())

x = d / v

print("No" if t <= x <= s else "Yes")