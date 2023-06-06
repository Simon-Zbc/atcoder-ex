n = int(input())
s = input()

l, m, r = -1, -1, -1
for i in range(n):
    if s[i] == "|" and l == -1:
        l = i
    elif s[i] == "|":
        r = i
    if s[i] == "*":
        m = i

if l < m and m < r:
    print("in")
else:
    print("out")