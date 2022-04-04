#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    int n, i, j, ans;
    int A[4005][3];
    int B[3];

    cin >> n >> B[0] >> B[1] >> B[2];

    for (i = 1; i <= n; i++) {
        for (j = 0; j < 3; j++) {
            if (i - B[j] < 0)
                A[i][j] = -1;
            else if (i - B[j] == 0)
                A[i][j] = 1;
            else {
                if (max(A[i - B[j]][0], max(A[i - B[j]][1], A[i - B[j]][2])) == -1) {
                    A[i][j] = -1;
                } else {
                    A[i][j] = max(max(A[i - B[j]][0], A[i - B[j]][1]), A[i - B[j]][2]) + 1;
                }
            }
        }
    }
    ans = max(max(A[n][0], A[n][1]), A[n][2]);
    cout << ans << '\n';
    return 0;
}