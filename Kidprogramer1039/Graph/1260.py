import sys
from collections import deque

input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:

        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                

node, line, start = map(int, input().split())
graph = [[] for _ in range(node+1)]  # 수정된 초기화

# 간선 입력
for _ in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (node+1)
dfs(start)
print()

visited = [False] * (node+1)
bfs(start)
