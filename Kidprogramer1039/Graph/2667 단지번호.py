import sys

input = sys.stdin.readline

def dfs(x, y):
    global count
    if x < 0 or x >= conNum or y < 0 or y >= conNum or country[x][y] == 0:  # 수정된 조건
        return False
    country[x][y] = 0
    count += 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True


result = []
conNum = int(input())
country = [list(map(int, input().rstrip())) for _ in range(conNum)]
for i in range(conNum):
    for j in range(conNum):
        count = 0
        if dfs(i,j):
            result.append(count)

print(len(result))
result.sort()
for res in result:
    print(res)
