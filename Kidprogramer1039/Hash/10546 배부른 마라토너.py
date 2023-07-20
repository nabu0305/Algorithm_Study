import sys

resp = []   
cnt = int(sys.stdin.readline())
dic = dict()
for _ in range(cnt):
    name = sys.stdin.readline().rstrip()
    if name in dic:
        dic[name] = dic[name] + 1
    else:
        dic[name] = 1

for _ in range(cnt-1):
    name = sys.stdin.readline().rstrip()
    dic[name] = dic[name] - 1

dic_reverse = sorted(dic.items(), reverse=True, key=lambda item: item[1])
print(dic_reverse[0][0])
