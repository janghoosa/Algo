#include <iostream>
#include <cmath>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cout.tie(nullptr);
    bool prime[1000001];
    int M, N;
    cin >> M >> N;
    for (int i = 0; i <= N; i++) {
        prime[i] = true;
    }
    prime[1] = false;
    for (int i = 2; i <= sqrt(N) ; i++) {
        if (prime[i]) {
            for (int j = i * i; j <= N; j += i) {
                prime[j] = false;
            }
        }
    }
    for (int i = M; i <= N; i++) {
        if (prime[i]) {
            cout << i << "\n";
        }
    }
    return 0;
}