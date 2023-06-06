s = input()

i = 0
l = len(s)
while i < l:
    if s[i:i+2] == "hi":
        i += 2
        continue
    else:
        print("No")
        exit()

print("Yes")