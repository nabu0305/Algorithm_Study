import sys
from collections import deque
# 11:40 ~

input = sys.stdin.readline

def bfs(start, endPoint):
    global chon
    queue = deque([start])
    visited = [False] * (n+1)
    chon = 0

    while queue:
        node = queue.popleft()
        visited[node] = True  # 현재 노드를 방문 표시

        if node == endPoint:
            return chon  # 목표 노드에 도달한 경우 촌수 반환

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True  # 방문한 노드를 표시

        chon += 1
        
    return -1


chon = 0
n = int(input()) #인원 입력
x,y = map(int, input().split()) #촌수 입력
rep = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(rep):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(len(graph)):
    graph[i].sort()


result = bfs(x, y)
print(result)
