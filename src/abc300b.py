from collections import deque


h, w = map(int, input().split())
a, b = [], []

for _ in range(h):
    a.append(input())

for _ in range(h):
    b.append(input())

da = deque(a)
db = deque(b)

for i in range(h):
    da.rotate(-1)
    for k in range(w + 1):
        for j in range(h):
            da[j] = da[j][1:w] + da[j][:1]
            if da == db:
                print("Yes")
                exit()

print("No")