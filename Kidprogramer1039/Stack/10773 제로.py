#10773번 문제
#풀이 시간 : 11:43 ~ 11:51

import sys

input = sys.stdin.readline

rep = int(input())
stk = []
res = 0
for _ in range(rep):
    num = int(input())
    if num == 0:
        stk.pop()
    else:
        stk.append(num)

for i in stk:
    res += i

print(res)
