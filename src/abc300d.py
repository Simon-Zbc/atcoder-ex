import math

def prime(N):
    primes = []
    for i in range(2, N + 1):
        primes.append(i)
        for p in range(2, i):
            if i % p == 0:
                primes.remove(i)
                break
    return primes

n = int(input())
N = int(math.sqrt(n / 12))
l = prime(N)
s = len(l)
count = 0
for i in range(s-2):
    a = l[i] * l[i]
    for j in range(i+1, s-1):
        b = l[j]
        for k in range(j+1, s):
            c = l[k] * l[j]
            if a * b * c < n:
                count += 1

print(count)