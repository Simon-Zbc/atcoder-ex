n = int(input())
s = input()

l = s.count("o")
f = s.count("x")

if l >= 1 and f == 0:
    print("Yes")
else:
    print("No")