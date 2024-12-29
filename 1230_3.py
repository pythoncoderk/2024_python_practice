a, b, c, d = map(str, input().split())

t = int(a + b.zfill(2))
a = int(c + d.zfill(2))

print("Aoki" if t > a else "Takahashi")