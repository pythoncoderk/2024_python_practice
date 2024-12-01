l = [int(input()) for i in range(5)]
x = int(input())

for i in range(len(l)):
    for j in range(len(l)):
        if abs(l[i] - l[j]) > x:
            print(":(")
            exit()

print("Yay!")