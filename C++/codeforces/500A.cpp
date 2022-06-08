#include <iostream>
using namespace std;
int A[30005];

int main(){
    int n, t, i;
    cin >> n >> t;
    for (i = 1; i < n;i++){
        cin >> A[i];
    }
    i = 1;
    while(i<n){
        i = i + A[i];
        if(i==t)
            break;
    }
    if(i == t)
        cout << "YES\n";
    else
        cout << "NO\n";
    return 0;
}