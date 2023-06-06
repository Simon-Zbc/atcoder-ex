n = int(input())
s = input()

if n == 1:
    print(-1)
else:
    l, r = -1, -1
    res, x = 0, 0
    flg = False
    for i in range(n):
        if s[i] == "o":
            if i > 0:
                if s[i - 1] == "-":
                    flg = True
            x += 1
            if i == n - 1 and flg:
                res = max(res, x)
        else:
            res = max(res, x)
            x = 0
    print(-1 if res == 0 else res)