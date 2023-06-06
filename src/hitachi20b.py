a, b, m = map(int, input().split())

m_list = []
a_list = [int(x) for x in input().split()]
b_list = [int(x) for x in input().split()]
for _ in range(m):
    m_list.append([int(x) for x in input().split()])

a_min, b_min = min(a_list), min(b_list)
total = a_min + b_min
for item in m_list:
    a_v, b_v = a_list[item[0] - 1], b_list[item[1] - 1]
    total = min(total, a_v + b_v - item[2])

print(total)