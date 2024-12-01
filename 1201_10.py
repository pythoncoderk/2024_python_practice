n, m = map(int, input().split())
s = list(input())

x = s[m - 1]
x_2 = chr(ord(x) + 32)

s[m - 1] = x_2

print("".join(s))


