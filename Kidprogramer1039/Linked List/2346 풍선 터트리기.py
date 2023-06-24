from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
l = list(map(int,input().split()))
ans = []
q = deque()


for idx,val in enumerate(l):
    q.append([val,idx+1])

while q:
    v = q.popleft()
    ans.append(v[1])
    if v[0]>0:
        q.rotate(-v[0]+1)
    else:
        q.rotate(-v[0])

print(*ans)
