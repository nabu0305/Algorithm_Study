import sys
from collections import deque

num = int(sys.stdin.readline())
a = deque()

for i in range(1, num+1):
    a.append(i)
   

while len(a) > 1:
    a.popleft()
    a.append(a.popleft())

print(a[0])
