#include <iostream>
#include <string>

using namespace std;

int main(){
    string input;
    cin >> input;

    for (string::iterator iter = input.begin(); iter != input.end();++iter){
        char temp = *iter;
        if(temp >= 'A' && temp <= 'Z'){
            temp = temp - ('A' - 'a');
        }
        if (temp != 'a' && temp != 'o' && temp != 'y' && temp != 'e' && temp != 'u' && temp != 'i') {
            cout << '.' << temp;
        } else {
            continue;
        }
    }

    return 0;
}