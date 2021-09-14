#include <iostream>
#include <algorithm>
using namespace std;

int input[9];
int num = 9;

int main() {
    int sum = 0;
    for (int i = 0; i < num; i++) {
        cin >> input[i];
        sum += input[i];
    }
    sort(input, input + num);
    for (int i = 0; i < num; i++) {
        for (int j = i; j < num; j++) {
            if (sum - input[i] - input[j] == 100) {
                for (int k = 0; k < num;k++){
                    if((k==i)||(k==j)){
                        continue;
                    }
                    cout << input[k] << "\n";
                }
                return 0;
            }
        }
    }

    return 0;
}