h, w = map(int, input().split())
a = []
for i in range(h):
    a.append([int(x) for x in input().split()])

row_sum = []
col_sum = []

for i in range(h):
    row_sum.append(sum(a[i]))

for j in range(w):
    col_total = 0
    for i in range(h):
        col_total += a[i][j]
    col_sum.append(col_total)

for i in range(h):
    res = ""
    for j in range(w):
        ans = row_sum[i] + col_sum[j] - a[i][j]
        res += str(ans) + " "
    print(res)
