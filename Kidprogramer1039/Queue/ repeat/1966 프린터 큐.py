import sys
from collections import deque

rep = int(sys.stdin.readline().rstrip())


for i in range(rep):
    n, m = map(int, sys.stdin.readline().split())
    origin = deque(map(int, sys.stdin.readline().split()))
    x = deque(sorted(origin, reverse=True))
    y = deque([0] * n)
    y[m] = "target"
    pr = 0
    while True:
        if n == 1:
            print(1)
            break
        else:
            if x[0] == origin[0] and y[0] == "target":
                pr += 1
                print(pr)
                break
            elif x[0] == origin[0] and y[0] == 0:
                x.popleft()
                origin.popleft()
                y.popleft()
                pr += 1
                continue
            elif x[0] != origin[0]:
                origin.append(origin.popleft())
                y.append(y.popleft())
                continue
