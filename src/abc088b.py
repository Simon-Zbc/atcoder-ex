n = input()
a = [int(x) for x in input().split()]
a.sort(reverse=True)
dif, i, length = 0, 0, len(a)
while i < length:
    if length - i > 1:
        dif += (a[i] - a[i + 1])
    else:
        dif += a[i]
    i += 2
print(dif)