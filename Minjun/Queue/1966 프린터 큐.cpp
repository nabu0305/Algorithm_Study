#include <iostream>
#include <queue>
using namespace std;
#define _CRT_SECURE_NO_WARNINGS
int n,m,t;

int main()
{
    cin >> t;
    for(int i=0;i<t;i++){
        int cnt = 0;
        cin >> n >> m;
        priority_queue<int>pq; //높은순대로 내림차순 되기때문에 사용하고
        queue<pair<int,int>>q;//위치와 값을 동시에 저장하기위에 pair 사용
        for(int j=0;j<n;j++){
            int a;
            cin >> a;
            q.push({j,a});
            pq.push(a);
        }
        while(!q.empty()){
            int location = q.front().first; //위치랑 값을 미리 저장한다
            int value = q.front().second;
            q.pop();
            
            if(pq.top() == value){ //탑에는 가장 높은값이 있기때문에 q에 value랑 같은 값이 되면 pop하면 된다.
                pq.pop();
                ++cnt;
                if(m == location){ //원하던 위치에 값이 pop되면 while 탈출하고 카운트 출력
                    cout << cnt << '\n';
                    break;
                }
            }
            else{
                q.push({location,value});
            } 
                
        }
    }
}
