#include <iostream>
#include <algorithm>

using namespace std;
typedef long long ll;
int A[100005];
ll D[2][100005];

int main(){
    int i, n;
    ll ans;
    cin >> n;
    for (i = 0; i < n;i++){
        cin >> A[i];
    }
    sort(A, A + n);
    D[0][0] = 0;
    D[1][0] = A[0];
    for (i = 1; i < n;i++){
        if(A[i-1] == A[i]){
            D[0][i] = D[0][i - 1];
            D[1][i] = D[1][i - 1] + A[i];
        } else if(A[i] == A[i-1]+1){
            D[0][i] = max(D[0][i - 1], D[1][i - 1]);
            D[1][i] = D[0][i - 1] + A[i];
        } else {
            D[0][i] = max(D[0][i - 1], D[1][i - 1]);
            D[1][i] = max(D[0][i - 1], D[1][i - 1])+A[i];
        }
    }
    ans = max(D[0][n - 1], D[1][n - 1]);
    cout << ans << '\n';
    return 0;
}