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
        if i == 'R': #reverse일 경우 1로 바꾸고, 아닐 경우 0으로 되돌리기(True False 이용)
            reverse = 1 - reverse
        else:
            if not arr: #Error일 경우 Error 플래그를 True로 변경
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
