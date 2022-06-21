#include <iostream>
#include <vector>
using namespace std;
int arr[105];
int main() {
    int n, m, k, i, j, tmp, ans;
    cin >> n;
    vector<int> V;
    for (i = 0; i < n; i++) {
        cin >> m;
        ans = 0;
        for (j = 0; j < m;j++){
            cin >> tmp;
            arr[j] = tmp;
        }
        for (j = 0; j < m;j++){
            for (k = j+1; k < m;k++){
                ans += (arr[j] % arr[k]);
                ans += (arr[k] % arr[j]);
            }
        }
        cout << '#' << i + 1 << ' ' << ans << '\n';
    }
}