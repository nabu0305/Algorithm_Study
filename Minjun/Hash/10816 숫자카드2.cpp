#include<iostream>
#include<algorithm>
using namespace std;
	
int m,n;
int a[500002];


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> m;
	for (int i = 0;i < m;i++) {
		cin >> a[i];
	}
	cin >> n;
	sort(a, a + m);
	while (n--) {
		int target;
		cin >> target;
		cout << upper_bound(a, a + m, target) - lower_bound(a, a + m, target) << '\n';
	}
}
