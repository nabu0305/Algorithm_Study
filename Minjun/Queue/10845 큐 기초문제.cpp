#include <iostream>
using namespace std;
#include<queue>

int n;
queue < int >q;

int main (){
  cin >> n;
  for (int i = 0; i < n; i++){
      string s;
      cin >> s;
    if (s == "push"){
	    int a;
	    cin >> a;
	    q.push (a);
	}
	else if (s=="size") cout << q.size() << '\n';
    else if (s == "front"){
        if (q.empty ()) cout << -1 << '\n';
        else cout << q.front() << '\n';
    }
    else if (s == "back"){
        if (q.empty ()) cout << -1 << '\n';
        else cout << q.back() << '\n';
    }
    
    else if (s == "empty"){
	    if (q.empty ()) cout << 1 << '\n';
	    else cout << 0 << '\n';
    }
    else if (s == "pop"){
	    if (q.empty())cout << -1 << '\n';
	    else{
	        cout << q.front() << '\n';
	        q.pop ();
	        }
	    }
    }
}
