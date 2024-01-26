#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;
#define MAX 102

int cnt = 0;
string arr[MAX];
bool vis[MAX][MAX];
queue<pair<int,int>>q;
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
int n;
vector<int> v;
int ans = 0;
void bfs(int x,int y){
    ans++;
    vis[x][y] = true;
    q.push({x,y});
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for(int dir=0;dir<4;dir++){
            int nx = dx[dir] + x;
            int ny = dy[dir] + y;
            if(nx < 0 || ny < 0 || nx >=n || ny >= n)continue;
            if(vis[nx][ny] == true || arr[nx][ny] == '0')continue;
            q.push({nx,ny});
            vis[nx][ny] = true;
            cnt++;
        }
    }
}

int main()
{
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(arr[i][j] == '1' && vis[i][j] == false){
                cnt = 1;
                bfs(i,j);
                v.push_back(cnt);
            }
        }
    }
    cout << ans << '\n';
    sort(v.begin(),v.end());
    for(int i=0;i<v.size();i++){
        cout << v[i] << '\n';
    }
}
