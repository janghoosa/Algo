#include <iostream>
#include <algorithm>

using namespace std;
int A[1000005], dp[1000005];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, i, a;
    cin >> n;

    for (i = 0; i < n; i++) {
        cin >> a;
        cin >> A[a];
    }
    if (A[0] != 0) {
        dp[0] = 1;
    }
    int ans = 0;
    for (i = 1; i < 1000005; i++) {
        if (A[i] == 0) {
            dp[i] = dp[i - 1];
        } else {
            if (A[i] >= i)
                dp[i] = 1;
            else
                dp[i] = dp[i - A[i] - 1] + 1; 
        }
        if (ans < dp[i]) {
            ans = max(ans, dp[i]);
            // cout << i <<" ans:" << ans << "    " << dp[i] << '\n';
        }
    }
    cout << n - ans << '\n';
    return 0;
}