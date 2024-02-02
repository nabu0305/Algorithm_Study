#include <iostream>
#include <queue>
using namespace std;

int F, S, G, U, D;

queue<int>q;
int dx[3];
int vis[1000002] = {0,};
bool flag = true;
int main()
{
    cin >> F >> S >> G >> U >> D;
    q.push(S);
    dx[0] = U;
    dx[1] = -D;
    vis[S] = 1;
    while(!q.empty()){
        int x = q.front();
        q.pop();
        for(int dir=0;dir<2;dir++){
            int nx = dx[dir] + x; 
            if(x == G){
                flag = false;
                break;
                
            }
            if(nx <= 0 || nx >F || vis[nx] > 0)continue;
            vis[nx] = vis[x] + 1;
            q.push(nx);
            
            
        }
    }
    if(flag)cout << "use the stairs";
    else cout << vis[G]-1;
}
