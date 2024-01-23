#include <iostream>
#include <queue>

using namespace std;
int N,M,V;
int arr[1002][1002];
bool vis[1002];
queue<int> q;
void dfs(int V){
    vis[V] = true;
    cout << V << ' ';
    for(int i=1;i<=N;i++){
        if(arr[V][i] == 1){
            if(!vis[i]){
                dfs(i);
            }
        }
    }
    
    
}

void bfs(int V){
    vis[V] = true;
    cout << V << ' ';
    q.push(V);
    
    while(!q.empty()){
        int y = q.front();
        q.pop();
        for(int i=1;i<=N;i++){
            if(arr[y][i] == 1 && vis[i]==false){
                q.push(i);
                vis[i] = true;
                cout << i << ' ';
            }
        }
    }
    
}

int main()
{
    
    cin >> N >> M >> V;
    while(M--){
        int a, b;
        cin >> a >> b;
        arr[a][b] = 1;
        arr[b][a] = 1;
    }
    
    dfs(V);
    cout << '\n';
    for(int i = 1;i<=N;i++){
        vis[i] = false;
    }
    bfs(V);
    
}
