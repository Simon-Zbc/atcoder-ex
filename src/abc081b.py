k = input()
a = [int(x) for x in input().split()]
flg = True
count = 0
while flg:
    for i, n in enumerate(a):
        if n % 2 == 1:
            flg = False
            break
        else:
            a[i] = n / 2
    if flg:
        count += 1
print(count)