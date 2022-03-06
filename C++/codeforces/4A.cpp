#include <iostream>
using namespace std;

int main(){
    int input;
    cin >> input;
    if(input<4){
        cout << "NO\n";
    }
    else if(input%2==0){
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
    return 0;
}