#include <iostream>
#include <stack>
using namespace std;

int main()
{
    int k;
    cin >> k;
    stack<int>s;
    int sum = 0;
    for(int i=0;i<k;i++){
        int a;
        cin >> a;
        if(a == 0)s.pop();
        else{
            s.push(a);
        }
    }
    while(!s.empty()){
        sum += s.top();
        s.pop();
    }
    cout << sum;
}
