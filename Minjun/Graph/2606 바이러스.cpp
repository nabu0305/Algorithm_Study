#include <iostream>
using namespace std;
#define MAX 102

int arr[MAX][MAX];
bool vis[MAX];
int n,m;
int cnt = 0;
int dfs(int x){
    vis[x] = true;
    for(int i = 1; i<=n;i++){
        if(arr[x][i] == 1 && vis[i] == false){
            vis[i] = true;
            cnt++;
            dfs(i);
            
        }
    }
    return cnt;
}

int main()
{
    cin >> n;
    cin >> m;
    for(int i=0;i<m;i++){
        int x,y;
        cin >> x >> y;
        arr[x][y] = 1;
        arr[y][x] = 1;
    }
    cout << dfs(1);
}
