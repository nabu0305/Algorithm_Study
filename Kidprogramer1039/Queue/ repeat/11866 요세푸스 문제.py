import sys
from collections import deque

n, k = sys.stdin.readline().split()
result = deque()
arr = deque()

for i in range(1, int(n)+1):
    arr.append(i)

while len(arr) > 0:
    for i in range(int(k)-1):
        arr.append(arr.popleft())
    result.append(arr.popleft())

list_str = str(result)[7:-2]
print("<"+list_str+">")
