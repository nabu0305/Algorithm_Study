#include <iostream>  
#include <string>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

set<string> set1;
int n;


int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    while(n--){
        string name,enter;
        cin >> name >> enter;
        if(enter == "enter"){
            set1.insert(name);
        }
        else{
            set1.erase(name);
        }
    }
    
    for(auto pos1 = set1.rbegin();pos1 != set1.rend();pos1++){
        cout << *pos1 << '\n';
    }
}
