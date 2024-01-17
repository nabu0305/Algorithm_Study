#include <iostream>
#include <queue>
#include <algorithm>
#define MAX 1002
using namespace std;


int dp[MAX][MAX];
int visited[MAX][MAX];
int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    queue<pair<int, int>>q;
    int N, M;
    cin >> N >> M;
    for (int i = 0;i < M;i++) {
        for (int j = 0;j < N;j++) {
            cin >> dp[i][j];
            if (dp[i][j] == 1)q.push({ i,j });
            if (dp[i][j] == 0)visited[i][j] = -1;
        }
    }

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0;i < 4;i++) {
            int nx = dx[i] + x;
            int ny = dy[i] + y;

            if (nx < 0 || ny < 0 || nx >= M || ny >= N)continue;
            if (visited[nx][ny] >= 0)continue;
            visited[nx][ny] = visited[x][y] + 1;
            q.push({ nx,ny });
        }
    }
    int ans = 0;
    for (int i = 0;i < M;i++) {
        for (int j = 0;j < N;j++) {
            if (visited[i][j] == -1) {
                cout << -1;
                return 0;
            }
            ans = max(ans, visited[i][j]);
        }
    }
    cout << ans;
}
