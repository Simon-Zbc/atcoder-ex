import collections

n = input()
a = [int(x) for x in input().split()]

if n == 1:
    print(0)
else:
    c = collections.Counter(a)
    res = 0
    for i in c.values():
        q, mod = divmod(i, 2)
        res += q
    print(res)