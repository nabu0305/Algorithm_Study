from collections import deque

def bfs(start, end):
    # 시작 위치부터 도착 위치까지의 최소 이동 횟수를 기록할 배열
    visited = [False] * 100001
    queue = deque([(start, 0)])  # (위치, 이동 횟수)

    while queue:
        current_pos, time = queue.popleft()  # 현재 위치와 이동 횟수
        if current_pos == end:  # 도착 위치에 도달하면 이동 횟수 반환
            return time
        # 다음에 이동할 위치가 범위 안에 있고, 방문한 적이 없으면 큐에 추가
        for next_pos in (current_pos - 1, current_pos + 1, current_pos * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

# 시작 위치와 도착 위치 입력 받기
start, end = map(int, input().split())
print(bfs(start, end))
----------------
# 내 풀이(틀린 거)

import sys

# 11:44 ~ 12:15

input = sys.stdin.readline

dp = [100001] * 100001

n, m = map(int, input().split())

dp[n] = 0

for i in range(n, 0, -1):
    if i > 0:
        dp[i-1] = min(dp[i-1], dp[i]+1)

for i in range(0, m+1):
    if dp[i] != 100001:
        if i > 0:
            dp[i-1] = min(dp[i-1], dp[i]+1)
        if i < 100001:
            dp[i+1] = min(dp[i+1], dp[i]+1)
        if i < 50001:
            dp[i*2] = min(dp[i*2], dp[i]+1)



print(dp[m])
