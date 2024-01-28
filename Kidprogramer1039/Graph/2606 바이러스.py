import sys
from collections import deque

# 11:25~ 11:33
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    infested.append(start)

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

computer = int(input())
line = int(input())

graph =[[] for _ in range(computer+1)]
infested = []
visited = [False] * (computer+1)

for i in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs(1)
print(len(infested)-1)
