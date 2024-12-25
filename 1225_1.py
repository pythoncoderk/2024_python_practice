s = input()
a, b, c = s[0], s[1], s[2]

print(int(a + b + c) + int(b + c + a) + int(c + a + b))