s = input()

b = s.find("B")
rb = s.rfind("B")

if (rb - b) % 2 != 1:
    print("No")
    exit()

r = s.find("R")
rr = s.rfind("R")
k = s.find("K")

if not (r < k and k < rr):
    print("No")
    exit()

print("Yes")