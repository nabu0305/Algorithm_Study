import sys

dic = dict()
res = []
n = int(sys.stdin.readline())

for string in range(n):
    a,b = sys.stdin.readline().rstrip().split()
    dic[a] = b

for i in dic.keys():
    if dic[i] == 'leave':
        continue
    elif dic[i] == 'enter':
        res.append(i)

res.sort(reverse=True)
        
for i in res:
    print(i)
