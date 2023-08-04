#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

unordered_set<string> US;
vector<int> DECK;
int N, P, cnt = 0;
bool USED[10];

void f(vector<int> V, int D)
{
    if (D == P)
    {
        string res = "";
        for (int k = 0; k < P; k++)
            res += to_string(DECK[k]);
        US.insert(res);
        return;
    }
    for (int i = 0; i < N; i++)
    {
        if (!USED[i])
        {
            USED[i] = true;
            DECK.push_back(V[i]);
            f(V, D + 1);
            DECK.pop_back();
            USED[i] = false;
        }
    }
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> P;
    vector<int> V(N);

    for (int i = 0; i < N; i++)
        cin >> V[i];

    f(V, 0);
    for (auto s : US)
        cnt++;
    cout << cnt;
}
