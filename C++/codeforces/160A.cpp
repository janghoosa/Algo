#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int in, count, A[200], total = 0 , sum=0 , cnt;
    cin >> in;
    for (int i = 0; i < in;i++){
        cin >> A[i];
        total += A[i];
    }
    sort(A, A + in);
    sum = 0;
    cnt = 0;

    for (int i = in - 1; i >= 0;i--){
        sum += A[i];
        cnt++;
        if(sum > total/2)
            break;
    }
    cout << cnt << '\n';
}