#include <iostream>

using namespace std;

int main() {
    int in2, in3, in5, in6;
    int sum = 0;
    cin >> in2 >> in3 >> in5 >> in6;
    while (in6) {
        if ((in2 > 0) && (in5 > 0) && (in6 > 0)) {
            sum += 256;
            in2--;
            in5--;
            in6--;
        } else {
            break;
        }
    }
    while (in3) {
        if ((in2 > 0) && (in3 > 0)) {
            sum += 32;
            in2--;
            in3--;
        } else {
            break;
        }
    }
    cout << sum << "\n";
    return 0;
}