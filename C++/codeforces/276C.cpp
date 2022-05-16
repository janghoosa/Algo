#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
int times[200005];
int A[200005];
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, q, i, j;
    int L, R;
    cin >> n >> q;
    for (i = 0; i < n; i++) {
        cin >> A[i];
    }
    for (i = 0; i < q;i++){
        cin >> L >> R;
        times[L - 1] += 1;
        times[R] -= 1;
    }
    for (i = 1; i < n;i++){
        times[i] += times[i - 1];
    }
    sort(A, A + n);
    sort(times, times+n);
    ll ans = 0;
    for (i = 0; i < n; i++) {
        ans +=  (ll)A[i] * (ll)times[i];
    }
    cout << ans << '\n';
    return 0;
}