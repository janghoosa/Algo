#include <iostream>
#include <string>

using namespace std;

int main() {
    string input;
    getline(cin, input);
    int count = 0;
    bool flag = false;
    for (int i = 0; i < input.length(); i++) {
        if(input.at(i)!=' ' && !flag){
            flag = true;
            count++;
        } 
        if(input.at(i) == ' ' && flag) {
            flag = false;
        }
    }
    cout << count << endl;
}