# 15:13 시작 ~ 15:53
import sys
from collections import deque

def left(a, q): #좌측으로 돌렸을 경우 나오는 경우의 수
    result = 0
    while q[0] != a:
        q.append(q.popleft())
        result += 1
    q.popleft()
    return int(result)

def right(a, q): #좌측으로 돌렸을 경우 나오는 경우의 수
    result2 = 0
    while q[0] != a:
        q.appendleft(q.pop())
        result2 += 1
    q.popleft()
    return int(result2)

input = sys.stdin.readline
n, m = map(int, input().split())
want = list(map(int, input().split()))
que = deque(i for i in range(1, n+1))
answer = 0



for i in want:
    save = deque(que)
    x = left(i, que)
    y = right(i, save)
    if x <= y:
        answer += x
    else:
        answer += y

print(answer)
