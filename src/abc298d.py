from collections import deque

d = deque()
d.append("1")

q = int(input())

query_list = []

for _ in range(q):
    query_list.append([int(x) for x in input().split()])

for i in range(q):
    if query_list[i][0] == 1:
        d.append(str(query_list[i][1]))
    if query_list[i][0] == 2:
        d.popleft()
    if query_list[i][0] == 3:
        result = "".join(d)
        print(int(result) % 998244353)
