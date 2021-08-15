#include <iostream>
using namespace std;

int main() {
    bool prime[1001];
    for (int i = 0; i < 1000; i++) {
        prime[i] = true;
    }
    prime[1] = false;
    for (int i = 2; i * i <= 1000; i++) {
        if (prime[i]) {
            for (int j = i * i; j <= 1000; j += i) {
                prime[j] = false;
            }
        }
    }
    int count;
    cin >> count;
    int result = 0;
    while (count--) {
        int input;
        cin >> input;
        if (prime[input]) {
            result++;
        }
    }
    cout << result << endl;
    return 0;
}