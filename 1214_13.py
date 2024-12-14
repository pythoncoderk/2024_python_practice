a, b, c = map(int, input().split())

player = ""
flag = False
while a != 0 and b != 0:
    if flag == False:
        if c == 0:
            player = "t"
            flag = True
        else:
            player = "a"
            flag = True
    if player == "t":
        a -= 1
        player = "a"
    else:
        b -= 1
        player = "t"

if a == b:
    print("Aoki" if c == 0 else "Takahashi")
else:
    print("Takahashi" if a > b else "Aoki")

