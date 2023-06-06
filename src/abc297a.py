n, d = map(int, input().split())
t = [int(x) for x in input().split()]

for i in range(1, n):
    if t[i] - t[i - 1] <= d:
        print(t[i])
        exit()

print(-1)