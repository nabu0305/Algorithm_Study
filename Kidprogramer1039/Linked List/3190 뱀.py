import sys

input = sys.stdin.readline

from collections import deque

# 사과를 먹으면 뱀길이 늘어남
# 벽이나 자기지신의 몸과 부딪히면 게임 끝
# 뱀은 0,0 시작 길이는 1 처음엔 오른쪽

# 1.다음칸에 몸길이 늘려서 이동
# 2-1.사과가 있으면 사과 사라지고 꼬리는 그전칸 그대로
# 2-2.사과 없으면 꼬리를 끌고와서 몸길이 그전 그대로 유지

N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1

# 방향전환 횟수
L = int(input())
time_dic = {}
for i in range(L):
    X, C = input().split()
    time_dic[int(X)] = C

# 우하좌상
dx = [0, 1, 0, -1]  # 행
dy = [1, 0, -1, 0]  # 열

# 뱀 초기위치, 방향 초기
x, y, d = 0, 0, 0

# 뱀
snake = deque([])
time = 0
while True:
    # 뱀머리 현재 위치
    snake.append((x, y))
    time += 1

    x += dx[d]
    y += dy[d]
    # 벽에 부딪히거나 자기 몸과 부딪히면
    if x < 0 or x >= N or y < 0 or y >= N or arr[x][y] == 2:
        break
    # 벽이 아니면
    # 사과가 없다면
    if not arr[x][y]:
        # 꼬리 없애주고
        i, j = snake.popleft()
        arr[i][j] = 0

    arr[x][y] = 2

    if time in time_dic:
        # 만약 시계방향으로 돈다면
        if time_dic[time] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

print(time)
