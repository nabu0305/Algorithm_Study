from collections import deque

def bfs(x, y, complex_num):
    global complex_size, complex_matrix, N

    queue = deque([(x, y)])
    complex_matrix[x][y] = complex_num
    size = 1

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N and complex_matrix[nx][ny] == 1:
                complex_matrix[nx][ny] = complex_num
                size += 1
                queue.append((nx, ny))

    return size

def find_complex():
    global complex_size, complex_matrix, N

    complex_num = 2

    for i in range(N):
        for j in range(N):
            if complex_matrix[i][j] == 1:
                size = bfs(i, j, complex_num)
                complex_size.append(size)
                complex_num += 1

def main():
    global complex_size, complex_matrix, N

    N = int(input())
    complex_matrix = [list(map(int, input().strip())) for _ in range(N)]
    complex_size = []

    find_complex()

    print(len(complex_size))
    for size in sorted(complex_size):
        print(size)

if __name__ == "__main__":
    main()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#추가 풀이
n=int(input())

array=[]

for i in range(n):
    array.append(list(map(int,input())))

home=[]
def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if array[x][y]==1:
        home.append(1)
        array[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
c=[]
count=0
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            count=count+1
            c.append(len(home))
            home=[]
            
c.sort()
print(count)
for i in c:
    print(i)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 틀린 코드
# 22:30 ~ 
import sys
from collections import deque

input = sys.stdin.readline

def cpxFinder(x,y): # 마을을 발견하고, 발견하면 값을 매기는 재귀 함수
    global villageNum, tempVil, a
    if x >= a or y >= a or x < 0 or y < 0:
        return
    else:
        if cpx[x][y] != 1:
            cpxFinder(x+1, y)
            cpxFinder(x, y+1)
        elif cpx[x][y] == 1:
            villageColoring(x,y)
            villageDetail.append((villageNum-1, tempVil))
            tempVil = 0
            villageNum += 1
    


def villageColoring(x,y): # 마을을 색칠하는 함수
    global a
    if x >= a or y >= a or x < 0 or y < 0:
        return
    else:    
        villageCount(x-1,y)
        villageCount(x+1,y)
        villageCount(x,y-1)
        villageCount(x,y+1)

def villageCount(x,y): # 색칠하는 세부 함수
    global villageNum, tempVil, a
    if x >= a or y >= a or x < 0 or y < 0:
        return
    else:
        if cpx[x][y] == 1:
            cpx[x][y] = villageNum
            tempVil += 1
            villageColoring(x,y)
        else:
            pass
    


def complexCount(a):
    cpxFinder(0, 0)



a = int(input())
villageDetail = [] #마을별 갯수 선행 저장
villageNum = 2 #마을 개수 세는 함수
tempVil = 0
result = []
cpx = []
for i in range(a):
    b = list(map(int, input().strip()))  # 각 줄을 정수 리스트로 변환
    cpx.append(b)
    
complexCount(a-1)
print(villageNum-2)
for i in villageDetail:
    result.append(i[1])

result.sort()
for i in result:
    print(i)
