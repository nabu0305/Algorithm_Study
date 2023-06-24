#include <iostream>
#include <list>
using namespace std;

int main()
{
    list<int>li1;
    list<int>li2;
    int n;
    cin >> n;
    for(int i=1;i<=n;i++){
        int a;
        cin >> a;
        li1.push_back(a);
        li2.push_back(i);
    }
    while(!li2.empty()){
        cout << li2.front() << " ";
        int idx = li1.front();
        li1.pop_front();
        li2.pop_front();
        if(li2.empty())break;
        if(li1.empty())break;
        if(idx > 0){
            for(int i=0;i<idx-1;i++){
                li1.push_back(li1.front());
                li1.pop_front();
                li2.push_back(li2.front());
                li2.pop_front();
            }
        }
        else{
            for(int i=0;i<(-1)*idx;i++){
                li1.push_front(li1.back());
                li1.pop_back();
                li2.push_front(li2.back());
                li2.pop_back();
            }
        }
        
    }
}
