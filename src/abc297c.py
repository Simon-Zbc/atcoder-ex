h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())

for i in range(h):
    s[i] = s[i].replace("TT", "PC")
    print(s[i])