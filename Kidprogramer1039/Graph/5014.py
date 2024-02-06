from collections import deque

def bfs(start, target, up, down, max_floor):
    visited = [False] * (max_floor + 1)
    queue = deque([(start, 0)])  # (현재 층, 버튼 클릭 수)

    while queue:
        current_floor, clicks = queue.popleft()

        if current_floor == target:
            return clicks

        # 올라가는 경우
        next_floor_up = current_floor + up
        if next_floor_up <= max_floor and not visited[next_floor_up]:
            visited[next_floor_up] = True
            queue.append((next_floor_up, clicks + 1))

        # 내려가는 경우
        next_floor_down = current_floor - down
        if next_floor_down >= 1 and not visited[next_floor_down]:
            visited[next_floor_down] = True
            queue.append((next_floor_down, clicks + 1))

    return "use the stairs"

# 입력 받기
F, S, G, U, D = map(int, input().split())

# BFS 호출
result = bfs(S, G, U, D, F)
print(result)
------------------------------
from collections import deque

#12:24 ~ 12:58

def bfs(f, start, end, u, d):
    # 시작 위치부터 도착 위치까지의 최소 이동 횟수를 기록할 배열
    visited = [False] * 10000001
    queue = deque([(start, 0)])  # (위치, 이동 횟수)

    while queue:
        current_pos, time = queue.popleft()  # 현재 위치와 이동 횟수
        if current_pos == end:  # 도착 위치에 도달하면 이동 횟수 반환
            return time
        # 다음에 이동할 위치가 범위 안에 있고, 방문한 적이 없으면 큐에 추가
        for next_pos in (current_pos - d, current_pos + u):
            if 0 <= next_pos <= f and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))
    return "use the stairs"

# 시작 위치와 도착 위치 입력 받기
f, start, end, u, d = map(int, input().split())
print(bfs(f, start, end, u, d))
