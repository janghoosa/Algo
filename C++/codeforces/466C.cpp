#include <iostream>

using namespace std;
long long A[500005];
long long B[500005];

int main() {
    long long in1, in2;
    long long total, tmp, cnt1;
    long long cnt;

    cin >> in1;
    B[0] = 0;
    for (long long  i = 0; i < in1; i++) {
        cin >> A[i];
        B[i + 1] = A[i] + B[i];
    }
    if (B[in1] % 3 != 0) {
        cnt = 0;
    } else {
        tmp = B[in1] / 3;
        cnt = 0;
        cnt1 = 0;
        for (long long  i = 1; i < in1; i++) {
            if(B[i] == (tmp*2)){
                cnt += cnt1;
            }
            if(B[i] == tmp){
                cnt1++;
            }
        }
    }
    cout << cnt << '\n';

    return 0;
}