n = int(input())
a = [int(x) for x in input().split()]

res = []

for i in range(n - 1):
    if a[i] + 1 < a[i + 1]:
        res.append(a[i])
        temp = a[i] + 1
        while temp < a[i + 1]:
            res.append(temp)
            temp += 1
    elif a[i] - 1 > a[i + 1]:
        res.append(a[i])
        temp = a[i] - 1
        while temp > a[i + 1]:
            res.append(temp)
            temp -= 1
    else:
        res.append(a[i])

res.append(a[-1])
print(*res)