#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;

int N;
queue<pair<int, int>>q;
vector<int>ans;
string dp[26];
bool visited[26][26];
int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };

void bfs(int row ,int col) {
    q.push({ row,col });
    visited[row][col] = true;
    int cnt = 0;
    cnt++;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0;i < 4;i++) {
            int nx = dx[i] + x;
            int ny = dy[i] + y;

            if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue;
            if (visited[nx][ny]== true || dp[nx][ny] =='0')continue;
            q.push({ nx,ny });
            visited[nx][ny] = true;
            cnt++;
        }
    }
    ans.push_back(cnt);
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    
    cin >> N;
    for (int i = 0;i < N;i++) {
        cin >> dp[i];
    }
    for (int i = 0;i < N;i++) {
        for (int j = 0;j < N;j++) {
            if (dp[i][j] == '0' || visited[i][j] == true)continue;
            bfs(i, j);
        }
    }
    
    sort(ans.begin(), ans.end());
    cout << ans.size() << '\n';
    for (int i = 0;i < ans.size();i++) {
        cout << ans[i] << '\n';
    }
}
