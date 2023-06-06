import sys

n = input()
s = input()
c = s.split(' ')

for i in c:
    if i == 'and' or i == 'not' or i == 'that' or i == 'the' or i == 'you':
        print('Yes')
        sys.exit()
        
print('No')