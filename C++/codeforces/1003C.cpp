#include <iostream>

using namespace std;

int A[5005];
int B[5005];

int main(){
    int in1, in2;
    cin >> in1;
    cin >> in2;
    B[0] = 0;
    for (int i = 0; i < in1; i++) {
        cin >> A[i];
        B[i+1] = B[i] + A[i];
    }
    double m = 0;
    for (int i = 0; i <= in1 - in2; i++) {
        for (int j = in2; j <= in1 - i; j++){
            double temp = (double)(B[i + j] - B[i]) / (double)(j);
            if (m < temp) {
                m = temp;
            }
        }
    }
    cout.precision(15);
    cout << m;
    return 0;
}