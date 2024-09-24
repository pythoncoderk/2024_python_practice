n = int(input())
for i in range(n):
    x = list(map(str, input().split()))
    print("User{")
    print(f"nickname : {x[0]}")
    print(f"old : {x[1]}")
    print(f"birth : {x[2]}")
    print(f"state : {x[3]}")
    print("}")