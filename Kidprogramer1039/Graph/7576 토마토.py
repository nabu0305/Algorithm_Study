import sys
from collections import deque

input = sys.stdin.readline

def judgement(x,y):
    if x >= w or y >= q or x < 0 or y < 0:
        return
    else:
        if box[x][y] == -1 or box[x][y] == 1:
            pass
        elif box[x][y] == 0:
            box[x][y] = 1
            tempList.append((x,y))


def tomatoRipe(lis): #익은 토마토의 상하좌우를 확인하는 함수
    x, y = lis
    # print(f"x,y = {x}, {y}")
    judgement(x-1, y)
    judgement(x+1, y)
    judgement(x, y-1)
    judgement(x, y+1)
    

def tomatoCount(n): #토마토의 상하좌우를 익게 만드는 함수
    result = 0 # 결괏값 함수 초기화

    for i in range(n): # 1일차 토마토가 익었는지 여부는 개별로 실행
        tomatoRipe(ripeTomatoes.popleft())

    if not tempList:
        return result

    while tempList:
        for _ in range(len(tempList)):
            a = tempList.popleft()
            # print(f"a = {a}")
            tomatoRipe(a)
        result += 1
        # print(f"tomatoCount TempList = {tempList}")
    return result
    
q, w = map(int, input().split()) #열, 행 개수 지정
box = []
for i in range(w):
    # 토마토 맵을 입력받고, 박스 배열에 저장
    a = list(map(int, input().split()))
    box.append(a)

rest_list = [list(filter(lambda x: box[j][x] == 1, range(q))) for j in range(w)]

# 비어있지 않은 위치를 좌표로 변환하여 저장
ripeTomatoes = deque([(i, j) for i, sublist in enumerate(rest_list) for j in sublist])

#토마토를 익히기 위한 임시 함수 지정
tempList = deque()

#토마토 함수 수행
resultValue = tomatoCount(len(ripeTomatoes))

zeroFind = 0
for in_list in box:
    if 0 in in_list:
        zeroFind += 1

if zeroFind != 0:
    print(-1)
else:
    print(resultValue)
