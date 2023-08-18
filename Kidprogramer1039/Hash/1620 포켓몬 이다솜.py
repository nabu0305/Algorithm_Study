import sys

def get_key(val):
    for key, value in dic.items():
         if val == value:
             return key

resp = []   
a,b = map(int, sys.stdin.readline().split())
dic = dict()
count = 1
for _ in range(a):
    monster = sys.stdin.readline().rstrip()
    dic[str(count)] = monster
    count += 1

dict_swap = {v:k for k,v in dic.items()}

for _ in range(b):
    target = sys.stdin.readline().rstrip()
    if target in dic:
        res = dic.get(target)
        resp.append(res)
    elif target in dict_swap:
        res = dict_swap.get(target)
        resp.append(res)

for i in resp:
    print(i)
