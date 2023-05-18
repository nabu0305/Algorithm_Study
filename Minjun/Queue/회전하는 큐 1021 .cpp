#include <iostream>
#include <deque>
#include<queue>
using namespace std;


deque<int>dq;
queue<int>q;
int n,m;
int point = 0;
int cnt = 0;

int main()
{
    cin >> n >> m;
    for(int i=1;i<=n;i++){
        dq.push_back(i);
    }
    for(int i=0;i<m;i++){
        int a;
        cin >> a;
        q.push(a);
    }
    while(!q.empty()){
        if(q.front() == dq.front()){
            dq.pop_front();
            q.pop();
        }
        else{
            for(int i=0;i<dq.size();i++){
                if(q.front()==dq[i]){
                    if(i>dq.size()/2){
                        dq.push_front(dq.back());
                        dq.pop_back();
                        cnt++;
                    }
                    else{
                        dq.push_back(dq.front());
                        dq.pop_front();
                        cnt++;
                    }
                }
            }
        }
    }
    cout << cnt;
}
