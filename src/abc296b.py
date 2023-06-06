data = []
col = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
}

for i in range(8):
    data.append(input())

for i in range(8):
    j = data[i].find("*")
    if j != -1:
        print("{}{}".format(col[j + 1], 8 - i))
        break