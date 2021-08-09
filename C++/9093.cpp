#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    int times;
    while (times--)
    {
        string input;
        getline(cin, input);
        input += '\n';
        stack<char> s;
        for(char ch : input) {
            if(ch == ' ' || ch == '\n') {
                while(!s.empty()){
                    cout << s.top();
                    s.pop();
                }
                cout << ch;
            } else {
                s.push(ch);
            }
        }
    }
    return 0;
}