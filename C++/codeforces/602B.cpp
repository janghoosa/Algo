#include <algorithm>
#include <iostream>
using namespace std;
int dp[100010];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, i, ans;
    cin >> n;
    ans = 0;
    for (i = 1; i <= n; i++) {
        int x;
        cin >> x;
        if (dp[x - 1] > dp[x + 1]) {
            // cout << ans << "  " << i << "  " << dp[x - 2] << "  " << dp[x + 1] << '\n';
            ans = max(ans, i - max(dp[x - 2], dp[x + 1]));
            
        } else {
            // cout << ans << "  " << i << "  " << dp[x + 2] << "  " << dp[x - 1] << '\n';
            ans = max(ans, i - max(dp[x + 2], dp[x - 1]));
        }
        dp[x] = i;
        // cout << x << ':' << i << '\n';
    }
    cout << ans << '\n';
}