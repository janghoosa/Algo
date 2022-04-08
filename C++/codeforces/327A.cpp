#include <iostream>
#include <algorithm>
using namespace std;
int n, ans;
int A[1000], B[1000], D[1000];

int main(){
    int i, mx;
    cin >> n;
    ans = 0;
    for (i = 0; i < n; i++) {
        cin >> A[i];
        if (A[i] == 1) {
            ans++;
            B[i] = -1;
        } else {
            B[i] = 1;
        }
    }
    D[0] = B[0];
    for (i = 1; i < n;i++){
        if(D[i-1]+B[i] > B[i])
            D[i] = D[i - 1] + B[i];
        else
            D[i] = B[i];
    }
    mx = -100;
    for (i = 0; i < n;i++){
        mx = max(mx, D[i]);
    }
    ans += mx;
    cout << ans << '\n';
    return 0;
}