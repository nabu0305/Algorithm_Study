import sys

res = []   
cnt = int(sys.stdin.readline())
dic = dict()

save = list(sys.stdin.readline().rstrip().split())

for i in save:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1

cnt2 = int(sys.stdin.readline())
check = list(sys.stdin.readline().rstrip().split())

for i in check:
    if i in dic:
        res.append(str(dic[i]))
    else:
        res.append(0)
cnt = 0
for i in range(0, len(res)-1):
    print(res[i], end=" ")
    cnt = i
print(res[cnt+1])
