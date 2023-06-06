n, a, b = map(int, input().split())
res = 0
for i in range(n + 1):
    s = str(i)
    l = list(map(int, s))
    t = sum(l)
    if t >= a and t <= b:
        res += i
print(res)