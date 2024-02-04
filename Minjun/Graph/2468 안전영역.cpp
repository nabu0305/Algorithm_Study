#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;
#define MAX 102

int arr[MAX][MAX];
int map[MAX][MAX];
int N,maxH = 0;
int cnt=0;
bool vis[MAX][MAX];
queue<pair<int,int>>q;
vector<int>v;
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

void bfs(int x,int y){
    q.push({x,y});
    vis[x][y] = true;
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for(int dir = 0;dir<4;dir++){
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if(nx > N || ny > N || nx < 0 || ny < 0)continue;
            if(vis[nx][ny] || !map[nx][ny])continue;
            q.push({nx,ny});
            vis[nx][ny] = true;
        }
    }
}

void reset() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            map[i][j] = 0;
            vis[i][j] = 0;
        }
    }
    cnt = 0;
}


int main()
{
    cin >> N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> arr[i][j];
            if(arr[i][j] > maxH)maxH = arr[i][j];
        }
    }
    for(int h = 1;h<=maxH;h++){
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(arr[i][j] < h){
                    map[i][j] = 0;
                }
                else{
                    map[i][j] = 1;
                }
               
            }
        }
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(map[i][j] == 1 && vis[i][j] == false){
                    bfs(i,j);
                    cnt++;
                }
            }
        }
        v.push_back(cnt);
        
        reset();
    }
    
    sort(v.begin(),v.end());
    cout << v[v.size() - 1];
   
}
