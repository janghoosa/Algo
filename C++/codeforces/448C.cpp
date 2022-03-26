#include <iostream>

using namespace std;

int solve(int A[], int in1) {
    int i, min, ans, p, q;
    min = 1000000005;
    for (i = 0; i < in1 ; i++){
        if(min > A[i]){
            min = A[i];
        }
    }
    for (i = 0; i < in1;i++){
        A[i] -= min;
    }
    ans = min;
    p = 0;
    while(p<in1){
        while (p < in1 && A[p] == 0) p++;
        if (p == in1) break;
        q = p;
        while (q + 1 < in1 && A[q + 1] > 0) q++;
        ans += solve(A + p, q - p + 1);
    }
    if (in1 > ans)
        return ans;
    else
        return in1;
};

int main() {
    int in1, ans;
    int A[5005];
    cin >> in1;
    for (int i = 0; i < in1;i++){
        cin >> A[i];
    }
    ans = solve(A, in1);
    cout << ans << '\n';
    return 0;
}