#include <cmath>
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    bool prime[1000001];
    for (int i = 0; i <= 1000000; i++) {
        prime[i] = true;
    }
    prime[1] = false;
    for (int i = 2; i <= sqrt(1000000); i++) {
        if (prime[i]) {
            for (int j = i * i; j <= 1000000; j += i) {
                prime[j] = false;
            }
        }
    }
    while (true) {
        int input;
        cin >> input;
        if(input == 0){
            break;
        }
        bool flag = false;
        for (int i = 2; i < input; i++) {
            if(prime[input-i]&&prime[i]){
                cout << input << " = " << i << " + " << input - i << "\n";
                flag = true;
                break;
            }
        }
        if(!flag){
            cout << "Goldbach's conjecture is wrong." << "\n";
        }
    }
    return 0;
}