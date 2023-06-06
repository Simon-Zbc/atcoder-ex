N = int(input())
t_pre, x_pre, y_pre = 0, 0, 0
flag = True
for _ in range(N):
    t, x, y = map(int, input().split())
    time = t - t_pre
    distance = abs(x - x_pre) + abs(y - y_pre)
    if time < distance:
        flag = False
    elif time % 2 != distance % 2:
        flag = False
    if not flag:
        break
    t_pre, x_pre, y_pre = t, x, y
if flag:
    print('Yes')
else:
    print('No')    