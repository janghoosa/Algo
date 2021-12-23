#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    string N;
    int cntBroken;
    cin >> N >> cntBroken;
    vector<int> broken(cntBroken);
    for (int i = 0; i < cntBroken;i++) {
        cin >> broken[i];
    }
    bool possible = true;
    for (int i = 0; i < N.size();i++){
        for (int j = 0; j < cntBroken; j++) {
            if (broken[j] == ((int)N.at(i))-'0') {
                possible = false;
            }
        }
    }
    cout << possible << "\n";
    return 0;
}