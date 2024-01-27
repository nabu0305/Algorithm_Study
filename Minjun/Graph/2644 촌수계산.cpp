#include <iostream>
#include <queue>
using namespace std;

int n,m;
int arr[102][102];
int vis[102];
queue<int>q;
int a,b;
int cnt =0;
void bfs(int x){
    q.push(x);
    vis[x] = 1;
    while(!q.empty()){
        int x = q.front();
        q.pop();
        for(int i=1;i<=n;i++){
            if(arr[x][i] == 1 && !vis[i]){
                vis[i] = vis[x] + 1;
                q.push(i);
                
            }
        }
    }
}

int main()
{
    cin >> n;
    cin >> a >> b;
    cin >> m;
    for(int i=0;i<m;i++){
        int x,y;
        cin >> x >> y;
        arr[x][y] = 1;
        arr[y][x] = 1;
    }
    bfs(b);
    if(vis[a] == 0)cout << -1;
    else cout << vis[a] - 1;
}
