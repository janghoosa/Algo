#include <iostream>
using namespace std;

int E[100005][3];
int F[100005];
int main() {
    int i, n, m, k, f, ans;
    cin >> n >> m >> k;
    for (i = 0; i < m; i++) {
        cin >> E[i][0] >> E[i][1] >> E[i][2];
    }
    for (i = 0; i < k; i++) {
        cin >> f;
        F[f] = 1;
    }
    ans = 2000000000;
    for (i = 0; i < m; i++) {
        if (F[E[i][0]] + F[E[i][1]] == 1) {
            ans = min(ans, E[i][2]);
        }
    }
    if (ans == 2000000000)
        cout << "-1\n";
    else
        cout << ans << '\n';
}