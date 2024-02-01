#include <iostream>
#include <queue>
using namespace std;
#define MAX 100002
int dx[] = {-1,1};
int N,K;
bool vis[MAX];
int main()
{
    cin >> N >> K;
    queue<pair<int,int>>q;
    q.push({N,0});
    while(!q.empty()){
        int x = q.front().first;
        int cnt = q.front().second;
        q.pop();
        if(x == K){
            cout << cnt;
            break;
        }
        if(x - 1 >= 0 && x - 1 <MAX){
            if(!vis[x-1]){
                q.push({x-1,cnt + 1});
                vis[x-1] = true;
            }
        }
        if(x + 1 >= 0 && x + 1 <MAX){
            if(!vis[x+1]){
                q.push({x+1,cnt + 1});
                vis[x+1] = true;
            }
        }
        if(x * 2 >= 0 && x * 2 <MAX){
            if(!vis[x*2]){
                q.push({x*2,cnt + 1});
                vis[x*2] = true;
            }
        }
    }
}
