#include <iostream>
#include <list>
using namespace std;

int main()
{
    int t1,t2,n,k;
    int map[102][102];
    bool vis[102][102];
    cin >> n;
    cin >> k;
    for(int i=0;i<k;i++){
        cin >> t1 >> t2;
        map[t1 - 1][t2 - 1] = 1;
    }
    int cnt = 0;
    char t3;
    int dx[4] = {1,0,-1,0};
    int dy[4] = {0,1,0,-1};
    int dir = 0;
    int x=0;
    int y=0;
    list<int>li1;
    list<int>li2;
    li1.push_back(x);
    li2.push_back(y);
    int bt1=0;
    int l;
    cin >> l;
    for(int i=0;i<l;i++){
        cin >> t1 >> t3;
        while(cnt < t1 || i == l-1){
            // 마지막 입력까지 게임이 끝나지 않을 경우 뱀을 끝날때까지 보내줘야함.
            cnt++;
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            
            if(nx >=0 && ny >=0 && nx<n && ny<n && !vis[ny][nx]){
                // 게임이 끝나지 않을 조건
                if(map[ny][nx] == 1){ // 사과를 먹었을 때
                    map[ny][nx] = 0; // 사과 없애주고
                    li1.push_back(nx);
                    li2.push_back(ny); // 몸 좌표에 추가
                    vis[ny][nx] = true; // 몸 있다는걸 좌표 표시
                }else{// 사과 없을 때
                    li1.push_back(nx);
                    li2.push_back(ny);
                    vis[ny][nx] = true; 
                    vis[li2.front()][li1.front()] = false;
                    // 꼬리 부분없애주기
                    li1.pop_front();
                    li2.pop_front();
                }
            }else{
                cout << cnt;
                return 0;
            }        
            x = nx;
            y = ny;
            if(cnt == t1){
                if(t3 == 'D'){ // 우측 회전
                    dir = (dir + 1) % 4; 
                }else{ // 좌측 회전
                    dir = (dir + 3) % 4;
                }
            }
        }
    }
}
