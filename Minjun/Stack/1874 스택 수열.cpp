#include <iostream>
#include<vector>
#include<stack>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int cnt = 1;
    stack<int>s;
    vector<char>answer;
    while(n--){
        int a;
        cin >> a;
        while(cnt <= a){
            s.push(cnt);
            cnt++;
            answer.push_back('+');
        }
        if(s.top() == a){
            s.pop();
            answer.push_back('-');
        }
        else{
            cout<<"NO";
            return 0;
        }
    }
    for(int i=0;i<answer.size();i++){
        cout << answer[i]<<'\n';
    }
}
