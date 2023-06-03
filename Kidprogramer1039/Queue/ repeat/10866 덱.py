import sys
from collections import deque

input = sys.stdin.readline
que = deque()
rep = int(input())
for i in range(rep):
    arr = list(map(str, input().split()))
    if arr[0] == "push_front":
        que.appendleft(arr[1])
    elif arr[0] == "push_back":
        que.append(arr[1])
    elif arr[0] == "pop_front":
        print('-1' if len(que) == 0 else que.popleft())
    elif arr[0] == "pop_back":
        print('-1' if len(que) == 0 else que.pop())
    elif arr[0] == "size":
        print(len(que))
    elif arr[0] == "empty":
        print('1' if len(que) == 0 else '0')
    elif arr[0] == "front":
        print('-1' if len(que) == 0 else que[0])
    elif arr[0] == "back":
        print('-1' if len(que) == 0 else que[len(que)-1])
