n, t = map(int, input().split())
c = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]

tn = []
for i in range(n):
    if c[i] == t:
        tn.append(i)

if len(tn) > 0:
    rn = r[tn[0]]
    res = tn[0]
    for i in range(len(tn)):
        if r[tn[i]] > rn:
            res = tn[i]
            rn = r[tn[i]]
    print(res + 1)
else:
    for i in range(n):
        if c[i] == c[0]:
            tn.append(i)
    rn = r[tn[0]]
    res = tn[0]
    for i in range(len(tn)):
        if r[tn[i]] > rn:
            res = tn[i]
            rn = r[tn[i]]
    print(res + 1)