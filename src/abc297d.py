a, b = map(int, input().split())

count = 0
while a != b:
    if a == 1 and b != 1:
        count += b - 1
        b = a
    elif a != 1 and b == 1:
        count += a - 1
        a = b

    if a > b:
        q, mod = divmod(a, b)
        count += q
        a = mod
    if a < b:
        q, mod = divmod(b, a)
        count += q
        b = mod
 
print(count)