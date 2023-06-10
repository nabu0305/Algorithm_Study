#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while(T--){
        string s;
        stack<char>c;
        string answer = "YES";
        cin >> s;
        for(int i=0;i<s.length();i++){
            if(s[i] == '(')c.push(s[i]);
            else if(!c.empty() && s[i] == ')' && c.top() == '(')c.pop();
            else{
                answer = "NO";
                break;
            }
        }
        if(!c.empty()){
            answer = "NO";
        }
        cout << answer << '\n';
    }
}
