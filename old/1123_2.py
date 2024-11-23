n = int(input())
m = input()

if n % 2 != 0:
    x = int(((n + 1) / 2) - 1)

    if m[:x].count("1") == x:

        if m[x] == "/":

            if m[x + 1:].count("2") == len(m[x + 1:]):
                print("Yes")
                exit()
print("No")




