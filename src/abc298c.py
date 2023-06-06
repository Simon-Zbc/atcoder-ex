n = int(input())
q = int(input())

query_list = []

for i in range(q):
    query_list.append([int(x) for x in input().split()])

n_box = []

for _ in range(n):
    n_box.append([])

res3 = {}

for i in range(q):
    if query_list[i][0] == 1:
        n_box[query_list[i][2] - 1].append(query_list[i][1])
        if query_list[i][1] in res3:
            res3[query_list[i][1]].add(query_list[i][2])
        else:
            res3[query_list[i][1]] = set([query_list[i][2]])
        continue
    if query_list[i][0] == 2:
        res2 = sorted(n_box[query_list[i][1] - 1])
        print(*res2)
        continue
    if query_list[i][0] == 3:
        res = sorted(res3[query_list[i][1]])
        print(*res)
        continue
