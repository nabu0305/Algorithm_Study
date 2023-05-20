#include <iostream>
using namespace std;
#include<deque>

int n;
deque <int>q; //deque가 다루기 쉬울거 같아서 일단 선택

int main (){
  cin >> n;
  for(int i=1;i<=n;i++){
      q.push_back(i);
  }
  while(true){
      if(q.size() == 1)break; //while문안에 조건을 넣으려고 했는데 if문 쓰는게 간단해서 씀
      q.pop_front(); //처음 카드를 빼고
      q.push_back(q.front()); // 맨앞 카드를 뒤로 넣고
      q.pop_front(); //맨앞 카드를 뒤로넣었으니깐 맨앞에 있는 카드를 한번 더 삭제
  }
  cout << q.front();
 
}
