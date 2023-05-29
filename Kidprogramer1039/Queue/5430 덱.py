from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    func = input().rstrip()
    num = int(input())
    arr = input().strip('[]\n').split(',')
    arr = deque(arr)

    reverse = 0
    error = 0

    if num == 0:
        arr = []

    for i in func:
        if i == 'R':
            reverse = 1 - reverse
        else:
            if not arr:
                error = 1
                break
            else:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
    if error:
        print('error')
    else:
        if reverse:
            arr.reverse()
            print(f"[{','.join(arr)}]")
        else:
            print(f"[{','.join(arr)}]")