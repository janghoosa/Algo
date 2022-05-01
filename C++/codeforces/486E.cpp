#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int n;
int A[100005];
int B[100005];
int L[100005];
int M[100005];
int R[100005];
int O[100005];
int LeftMax[100005];
int RightMin[100005];

vector<int> Last;

void LIS(int X[], int D[], int n) {
    int i;
    vector<int>::iterator it;
    Last.clear();
    Last.push_back(-1);
    for (i = 1; i <= n; i++) {
        if (Last.back() < X[i])
            Last.push_back(X[i]);
        it = lower_bound(Last.begin(), Last.end(), X[i]);
        *it = X[i];
        D[i] = it - Last.begin();
    }
}

int main() {
    int i;
    cin >> n;
    for (i = 1; i <= n; i++) {
        cin >> A[i];
    }
    LIS(A, L, n);
    // for (i = 0; i <= n; i++) {
    //     cout << L[i] << " ";
    // }
    // cout << '\n';

    for (i = 1; i <= n; i++) {
        B[n - i + 1] = 1000000 - A[i];
    }
    LIS(B, M, n);
    // for (i = 0; i <= n; i++) {
    //     cout << B[i] << " ";
    // }
    // cout << '\n';
    // for (i = 0; i <= n; i++) {
    //     cout << M[i] << " ";
    // }
    // cout << '\n';

    for (i = 1; i <= n; i++) {
        R[n - i + 1] = M[i];
    }
    // for (i = 0; i <= n; i++) {
    //     cout << R[i] << " ";
    // }
    // cout << '\n';
    
    int LMax;
    LMax = 0;
    for (i = 1; i <= n; i++) {
        LMax = max(LMax, L[i]);
    }
    // cout << "Lmax: " << LMax << '\n';
    for (i = 1; i <= n; i++) {
        O[i] = 1;
    }
    for (i = 1; i <= n; i++) {
        if (L[i] + R[i] == LMax + 1) {
            O[i] = 3;
        }
    }

    LeftMax[0] = -1;
    for (i = 1; i <= n; i++) {
        if (O[i] == 3)
            LeftMax[i] = max(LeftMax[i - 1], A[i]);
        else
            LeftMax[i] = LeftMax[i - 1];
    }
    RightMin[n + 1] = 1000000;
    for (i = n; i >= 1; i--) {
        if (O[i] == 3)
            RightMin[i] = min(RightMin[i + 1], A[i]);
        else
            RightMin[i] = RightMin[i + 1];
    }
    for (i = 1; i <= n; i++) {
        if (O[i] == 3 && (LeftMax[i - 1] >= A[i] || RightMin[i + 1] <= A[i]))
            O[i] = 2;
    }
    for (i = 1; i <= n; i++) {
        cout << O[i];
    }
    cout << '\n';
}