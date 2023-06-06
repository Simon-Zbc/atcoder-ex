n, x = map(int, input().split())
a = [int(x) for x in input().split()]

if x == 0:
    print("Yes")
    exit()

a = set(a)

for i in a:
    if (x + i) in a:
        print("Yes")
        exit()

print("No")