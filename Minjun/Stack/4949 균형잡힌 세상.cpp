#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main()
{
    while(1){
        string s;
        stack<char>c;
        getline(cin,s);
        if(s[0] == '.')break;
        for(int i=0;i<s.length();i++){
            if(s[i] == '(')c.push(s[i]);
            if(s[i] == '[')c.push(s[i]);
            if(s[i] == ')'){
                if(!c.empty() && c.top() == '(')c.pop();
                else{
                cout << "no" << '\n';
                break;
                }
            }
            if(s[i] == ']'){
                if(!c.empty() && c.top() == '[')c.pop();
                else{
                cout << "no" << '\n';
                break;
                }
            }
            if(!c.empty()&& i == s.length()-2) // 끝에 도달했는데 짝을 못맞췄으면 no{
            cout << "no" << '\n';
            }
            else if(c.empty()&& i == s.length()-2)cout << "yes" << '\n';
        }
        
    }
}
