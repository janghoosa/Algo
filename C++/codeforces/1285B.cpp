#include <iostream>

using namespace std;
typedef long long ll;
ll A[100005];
ll P[100005];
ll M[100005];

int main() {
    ll in1, in2, total, ans, min;
    cin >> in1;

    for (ll i = 0; i < in1; i++) {
        cin >> in2;
        P[0] = 0;
        for (ll j = 0; j < in2; j++) {
            cin >> A[j];
            P[j + 1] = P[j] + A[j];
        }
        total = P[in2];
        ans = 1;
        min = 0;
        for (ll j = 1; j < in2; j++) {
            M[j] = P[j] - min;
            if(min > P[j]){
                min = P[j];
            }
            if(M[j]>=total){
                ans = 0;
            }
        }
        for (ll j = 1; j <= in2;j++){
            P[j] -= A[0];
        }
        min = 0;
        for (ll j = 2; j <= in2;j++){
            M[j] = P[j] - min;
            if(min > P[j]){
                min = P[j];
            }
            if(M[j]>=total){
                ans = 0;
            }
        }
        if(ans == 1){
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}