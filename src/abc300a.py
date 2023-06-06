n, a, b = map(int, input().split())
c = [int(x) for x in input().split()]

print(c.index(a + b) + 1)