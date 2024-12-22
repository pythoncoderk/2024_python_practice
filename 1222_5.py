n = int(input())
total = 1
sub = 0
for i in range(3):
    l = list(map(int, input().split()))
    sub = sum(l)
    total *= sub
    sub = 0
print(total)
