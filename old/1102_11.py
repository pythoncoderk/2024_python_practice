N = int(input())
q, r = [0] * N, [0] * N
for i in range(N):
    q[i], r[i] = map(int, input().split())
Q = int(input())
for _ in range(Q):
    t, d = map(int, input().split())
    print(d + (r[t - 1] - d) % q[t - 1])
