import sys
from collections import deque

def solution(N, M, maze):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(0, 0, 1)])  # 시작 위치와 이동한 칸 수를 저장
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while queue:
        x, y, count = queue.popleft()

        if x == N - 1 and y == M - 1:
            return count

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    result = solution(N, M, maze)
    print(result)
