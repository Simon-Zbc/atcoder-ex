import math


a, b = map(int, input().split())
count = 0

while a > 0 and b > 0:
    g = math.gcd(a, b)
    a -= g
    b -= g
    count += 1

print(count)