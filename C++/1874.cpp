#include <iostream>
#include <stack>
#include <string>
using namespace std;
int main()
{
    stack<int> stack;
    int times;
    string ans;
    cin >> times;
    int m = 0;
    while (times--){
        int x;
        cin >> x;
        if (x > m) {
            while (x > m){
                stack.push(++m);
                ans += '+';
            }
            stack.pop();
            ans += '-';
        } else {
            bool found = false;
            if (!stack.empty()){
                int top = stack.top();
                stack.pop();
                ans += '-';
                if (x == top){
                    found = true;
                }
            }
            if (!found){
                cout << "NO" << '\n';
                return 0;
            }
        }
    }
    for (auto x : ans){
        cout << x << '\n';
    }
    return 0;
}