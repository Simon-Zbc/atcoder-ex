s = input()
t = input()

s_r = s.replace("@", "")
t_r = t.replace("@", "")

s_sort = sorted(s_r)
t_sort = sorted(t_r)

atcoder = ["a", "t", "c", "o", "d", "e", "r"]

s_sort_i, t_sort_i = 0, 0
while s_sort_i < len(s_sort) and t_sort_i < len(t_sort):
    if s_sort[s_sort_i] < t_sort[t_sort_i]:
        if s_sort[s_sort_i] in atcoder:
            t_sort.insert(t_sort_i, s_sort[s_sort_i])
        else:
            print("No")
            exit()
    elif s_sort[s_sort_i] > t_sort[t_sort_i]:
        if t_sort[t_sort_i] in atcoder:
            s_sort.insert(s_sort_i, t_sort[t_sort_i])
        else:
            print("No")
            exit()
    s_sort_i += 1
    t_sort_i += 1

if len(s_sort) != len(t_sort):
    apend_s = set(s_sort[s_sort_i:])
    apend_t = set(t_sort[t_sort_i:])
    for i in atcoder:
        if i in apend_s:
            apend_s.remove(i)
        if i in apend_t:
            apend_t.remove(i)
    if len(apend_s) == 0 and len(apend_t) == 0:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")