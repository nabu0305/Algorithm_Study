#덱을 이용한 풀이(18258번)
import sys
from collections import deque
data = int(sys.stdin.readline().rstrip()) # 줄바꿈 기호 삭제
result = deque()

for i in range(data):
    com = sys.stdin.readline().rstrip().split()
    if com[0] == 'push':
        result.append(int(com[1]))
    elif com[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.popleft())
    elif com[0] == 'size':
        print(len(result))
    elif com[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])
    elif com[0] == 'back':
        if len(result) == 0:
            print(-1)
        else:
            print(result[len(result)-1])

