import sys

res = []   
a,b = map(int, sys.stdin.readline().split())

dic = dict()

for i in range(a):
    site, id = sys.stdin.readline().rstrip().split()
    dic[site] = id

for i in range(b):
    tg = sys.stdin.readline().rstrip()
    res.append(dic[tg])

for i in res:
    print(i)
