#include <iostream>
using namespace std;
typedef long long ll;

ll C[100010];
string A[2], B[2];

string reverse(string s) {
    string res = s;
    int i, len = res.length();
    for (i = 0; i < len / 2; ++i)
        swap(res[i], res[len - 1 - i]);
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll n, i, j;
    ll c0, cr, c01, c02, cr1, cr2, p0, pr, ans;
    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> C[i];
    }
    cin >> A[0];
    A[1] = reverse(A[0]);
    c0 = 0;
    cr = C[0];
    B[0] = A[0];
    B[1] = A[1];
    p0 = c0;
    pr = cr;
    // cout << "p0:" << p0 << " pr:" << pr << '\n';
    for (i = 1; i < n; i++) {
        cin >> A[0];
        A[1] = reverse(A[0]);
        if (p0 == -1 && pr == -1) {
            c0 = -1;
            cr = -1;
        } else {
            c01 = -1;
            c02 = -1;
            if (A[0] >= B[0] && p0 != -1) c01 = p0;
            if (A[0] >= B[1] && pr != -1) c02 = pr;
            if (c01 == -1 && c02 == -1)
                c0 = -1;
            else if (c01 == -1 && c02 != -1)
                c0 = c02;
            else if (c01 != -1 && c02 == -1)
                c0 = c01;
            else
                c0 = min(c01, c02);
            cr1 = -1;
            cr2 = -1;
            if (A[1] >= B[0] && p0 != -1) cr1 = p0 + C[i];
            if (A[1] >= B[1] && pr != -1) cr2 = pr + C[i];
            if (cr1 == -1 && cr2 == -1)
                cr = -1;
            else if (cr1 == -1 && cr2 != -1)
                cr = cr2;
            else if (cr1 != -1 && cr2 == -1)
                cr = cr1;
            else
                cr = min(cr1, cr2);
        }
        B[0] = A[0];
        B[1] = A[1];
        p0 = c0;
        pr = cr;
        // cout << "p0:" << p0 << " pr:" << pr << '\n';
    }
    if (c0 == -1 && cr == -1)
        ans = -1;
    else if (c0 == -1 && cr != -1)
        ans = cr;
    else if (c0 != -1 && cr == -1)
        ans = c0;
    else
        ans = min(c0, cr);
    cout << ans << '\n';
    return 0;
}