#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;

int N,M;
queue<pair<int, int>>q;
int ans=0;
int dp[102][102];
int visited[102][102];
int dist[102][102];
int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };

void bfs(int row ,int col) {
    q.push({ row,col });
    visited[row][col] = 1;
    dist[row][col]++;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0;i < 4;i++) {
            int nx = dx[i] + x;
            int ny = dy[i] + y;

            if (nx < 0 || ny < 0 || nx >= N || ny >= M)continue;
            if (visited[nx][ny] == 1 || dp[nx][ny] == 0)continue;
            q.push({ nx,ny });
            dist[nx][ny] = dist[x][y] + 1;
            visited[nx][ny] = 1;
        }
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    
    cin >> N >>M;
    for (int i = 0;i < N;i++) {
        
        string row;
        cin >> row;
        for(int j=0;j<M;j++){
            dp[i][j] = row[j] - '0';
        }
    }
    bfs(0,0);
    cout << dist[N-1][M-1];
    
}
