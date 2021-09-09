#include <iostream>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    int count2 = 0, count5 = 0;
    for (long long i = 2; i <= N; i *= 2) {
        count2 += N / i;
    }
    for (long long i = 2; i <= N - M; i *= 2) {
        count2 -= (N - M) / i;
    }
    for (long long i = 2; i <= M; i *= 2) {
        count2 -= M / i;
    }
    for (long long i = 5; i <= N; i *= 5) {
        count5 += N / i;
    }
    for (long long i = 5; i <= N - M; i *= 5) {
        count5 -= (N - M) / i;
    }
    for (long long i = 5; i <= M; i *= 5) {
        count5 -= M / i;
    }

    if (count2 <= count5) {
        cout << count2;
    } else {
        cout << count5;
    }
    return 0;
}