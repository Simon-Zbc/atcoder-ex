n = int(input())
s = input()

count_t = s.count("T")
count_a = s.count("A")

if count_t > count_a:
    print("T")
elif count_t < count_a:
    print("A")
else:
    temp_t, tamp_a = 0, 0
    l = len(s)
    for c in s:
        if c == "T":
            temp_t += 1
        else:
            tamp_a += 1
        if temp_t == (l / 2):
            print("T")
            exit()
        if tamp_a == (l / 2):
            print("A")
            exit()