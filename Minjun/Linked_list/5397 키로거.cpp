#include <iostream>
#include<string>
#include<list>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    string L;
    while(T--){
        list<char>li(0);
        list<char>::iterator iter;
        iter = li.begin();
        li.clear();
        cin >> L;
        for(int i=0;i<L.length();i++){
            if(L[i]== '<'){
                if(iter != li.begin())iter--;
            }
            else if(L[i]== '>'){
                if(iter != li.end())iter++;
            }
            else if(L[i]=='-'){
                if(iter != li.begin()){
                    iter=li.erase(--iter);;
                    
                }
                
            }
            else{
                li.insert(iter,L[i]);
            }
        }
        for(iter=li.begin();iter != li.end();iter++){
            cout << *iter;
        }
        cout << '\n';
    }
}
