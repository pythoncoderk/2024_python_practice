s = input()
t = input()
flag = True
if s == t:
    print(0)
    exit()
else:
    s_l = len(s)
    t_l = len(t)
    if s_l < t_l:
        max_l = s_l
    else:
        max_l = t_l

    for i in range(max_l):
        if s[i] != t[i]:
            print(i + 1)
            flag = False
            break
if flag and len(s) != len(t):
    if s_l < t_l:
        print(s_l + 1)
        exit()
    else:
        print(t_l + 1)
        exit()
elif flag:
    print(0)
elif flag is False:
    pass
else:
    if s_l > t_l:
        print(t_l + 1)
    else:
        print(s_l + 1)