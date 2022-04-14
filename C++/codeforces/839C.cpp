#include <iostream>
#include <vector>
#include <iomanip> 
using namespace std;
int A[100005];
vector<int> v[100005];
double ans = 0.0;

void dfs(int nd, double prob, int deps) {
    int i, res, isGo;
    A[nd] = 1;
    isGo = 0;
    // cout << nd << "nd\n";
    for (i = 0; i < v[nd].size(); i++) {
        int go = v[nd][i];
        if (A[go] != 1) {
            isGo += 1;
        }
    }
    for (i = 0; i < v[nd].size(); i++) {
        int go = v[nd][i];
        if (A[go] != 1) {
            // cout << v[nd][i] << "\n";
            dfs(go, prob/isGo, deps+1);
        }
    }
    if (isGo == 0) {
        ans += (prob*deps);
    }
    A[nd] = 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int i, n, in, in2;
    cin >> n;
    for (i = 1; i < n; i++) {
        cin >> in >> in2;
        v[in].push_back(in2);
        v[in2].push_back(in);
    }
    dfs(1, 1 ,0);
    cout << fixed << setprecision(6) << ans;
}