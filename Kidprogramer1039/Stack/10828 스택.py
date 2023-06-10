#10828번 문제
#풀이 시간 : 10:01 ~ 10:12

import sys

input = sys.stdin.readline

rep = int(input())
li = []
res = []

for _ in range(rep):
    com = input().rstrip().split() #명령을 입력받고, 띄어쓰기를 기준으로 명령 구분
    t = com[0] #t라는 변수에 앞 명령어 저장
    if t == 'push':
        li.append(com[1])
    elif t == 'pop':
        if len(li) == 0:
            res.append('-1')
        else:
            res.append(li.pop())
    elif t == 'size':
        res.append(len(li))
    elif t == 'empty':
        res.append('1' if len(li) == 0 else '0')
    elif t == 'top':
        res.append('-1' if len(li) == 0 else li[-1])

for i in res: print(i)
