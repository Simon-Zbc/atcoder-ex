a, b = map(int, input().split())
res = 'Even' if a * b % 2 == 0 else 'Odd' 
print(res)