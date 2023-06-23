#include <iostream>
#include <list>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    string s;
    int m;
    list<char> li;
    list<char>::iterator iter;
    
    cin >> s;
    for(int i=0;i<s.length();i++){
        li.push_back(s[i]);
    }
    iter = li.end();
    cin >> m;
    while(m--){
        char c1;
        char c2;
        cin >> c1;
        if(c1 == 'P'){
            cin >> c2;
            li.insert(iter,c2);
            
        }
        else if(c1 == 'L'){
            if(iter != li.begin())iter--;
        }
         else if(c1 == 'D'){
            if(iter != li.end())iter++;
            
        }  
        else if(c1 == 'B'){
            if(iter != li.begin()){
                iter--;
                iter = li.erase(iter);
            }
        }
    }
    for(iter = li.begin();iter != li.end();iter++){
        cout << *iter;
    }
}
