n = int(input())
d = []
for i in range(n):
    d.append(int(input()))
d.sort(reverse=True)
res, i = 1, 0
while i < n - 1:
    if d[i] != d[i + 1]:
        res += 1
    i += 1
print(res)