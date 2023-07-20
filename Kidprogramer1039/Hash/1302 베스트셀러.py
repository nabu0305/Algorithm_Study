dic = dict()
res = []

n = int(input())

for _ in range(n):
    a = input()
    if a in dic.keys():
        dic[a] = dic[a] + 1
    else:
        dic[a] = 1

res = [k for k,v in dic.items() if max(dic.values()) == v]
res.sort()
print(res[0])
