#include <iostream>
#include <list>
using namespace std;

int main()
{
    int cnt = 1;
    list<int>li;
    int n,k;
    cin >> n >> k;
    for(int i=1;i<=n;i++){
        li.push_back(i);
    }
    cout << "<";
    while(1){
        if(li.size() == 1)break;
        if(cnt == k){
            cout << li.front() << ", ";
            li.pop_front();
            cnt = 1;
        }
        else{ //여기 코드가 원을 나타내는 코드
            cnt++;
            li.push_back(li.front());
            li.pop_front();
        }
    }
    cout << li.front() << ">";
}
