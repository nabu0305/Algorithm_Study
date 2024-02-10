import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y, k):
    global count
    if x < 0 or x >= conNum or y < 0 or y >= conNum or graph[x][y] == 0:  # 수정된 조건
        return False
    graph[x][y] = 0
    count += 1
    dfs(x-1, y,k)
    dfs(x+1, y,k)
    dfs(x, y-1,k)
    dfs(x, y+1,k)
    return True


result = []
final = []
conNum = int(input())
country = []
maxsize = 0
for _ in range(conNum):
        a = list(map(int, input().split()))
        if max(a) >= maxsize:
            maxsize = max(a)
        country.append(a)
        
for k in range(conNum-1):
    graph = copy.deepcopy(country)
    for i in range(conNum):
        for j in range(conNum):
            count = 0
            if dfs(i,j,k):
                result.append(count)
    final.append(len(result))


print(max(final))
