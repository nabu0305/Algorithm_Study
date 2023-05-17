#include<queue>
#include <iostream>

using namespace std;


queue<int>q;
int n,k;

int main()
{
    cin >> n >> k;
    for(int i=1;i<=n;i++){
        q.push(i);// 1234567 순서대로 넣어줌
    }
    cout << "<";
    while(q.size() != 0){
        for(int i=1;i<k;i++){
            q.push(q.front());
            q.pop();
        }
        cout << q.front();
        if(q.size() != 1)cout << ", ";
        q.pop();
    }
    cout << ">";
}
