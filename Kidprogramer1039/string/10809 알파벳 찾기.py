import sys

s = sys.stdin.readline().rstrip()
dic = dict()
alphabet = "abcdefghijklmnopqrstuvwxyz"
cnt = 0
result = []

for i in s: #주어진 단어의 값을 dictonary 형식으로 저장 
    if i in dic:
        cnt += 1
        pass
    else:
        dic[i] = cnt
        cnt += 1
        
        
for i in alphabet:
    if i in dic:
        result.append(dic[i])
    else:
        result.append(-1)

print(*result)
