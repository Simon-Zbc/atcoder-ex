n = int(input())
 
if n % 2 != 0:
    print('')
    exit()
 
l, r, res = n/2, n/2, []
 
def dfs(l, r, res, s):
    if r < l:
        return
    if not l and not r:
        res.append(s)
        return
    if l:
        dfs(l - 1, r, res, s + '(')
    if r:
        dfs(l, r - 1, res, s + ')')
 
dfs(l, r, res, '')
 
for c in res:
    print(c)