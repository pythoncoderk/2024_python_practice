n, m = map(int, input().split())

l = [list(map(int, input().split())) for i in range(m)]
l.append([])

print(l)


def dfs(pos):
    for i in l[pos]:
        dfs(i)

dfs(0)