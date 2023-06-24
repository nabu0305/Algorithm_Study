#include <iostream>
#include <list>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
	cin.tie(0);
    int left,right;
    list<int>li;
    int n,m;
    int cnt = 0;
    cin >> n >> m;
    for(int i=1;i<=n;i++){
        li.push_back(i);
    }
     
    while(m--){
        list<int>::iterator iter = li.begin();
        int num;
        cin >> num;
        for(int i=0;i<li.size();i++){
            
            if(*iter == num){
                left =  i;
                right = li.size()-i;
                break;
            }
            iter++;
        }
        if(left <=right){
            while(1){
                if(li.front() == num)break;

                li.push_back(li.front());
                li.pop_front();
                cnt++;
            }
            li.pop_front();
        }
        else{
            cnt++;
            while(1){
                if(li.back() == num)break;
                
                li.push_front(li.back());
                li.pop_back();
                cnt++;
            }
            li.pop_back();
        }
    }
    cout << cnt;
}
