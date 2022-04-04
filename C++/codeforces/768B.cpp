#include <iostream>
using namespace std;
typedef long long ll;

ll solve(ll in1, ll l, ll r) {
    ll n, mid, length, center;
    n = in1 / 2;
    length = 1;
    while (n > 0) {
        length = length * 2 + 1;
        n /= 2;
    }

    if (l == 1 && r == length) {
        return in1;
    }

    mid = (length + 1) / 2;
    center = in1 % 2;
    if (l > mid) return solve(in1 / 2, l - mid, r - mid);
    if (r < mid) return solve(in1 / 2, l, r);
    if (l == mid && r == mid) return in1 % 2;
    if (l == mid) return solve(in1 / 2, 1, r - mid) + center;
    if (r == mid) return solve(in1 / 2, l, mid - 1) + center;
    return solve(in1 / 2, l, mid - 1) + solve(in1 / 2, 1, r - mid) + center;
};

int main() {
    ll in1, in2, in3;
    cin >> in1 >> in2 >> in3;

    cout << solve(in1, in2, in3) << '\n';
    return 0;
}