#include <iostream>
#include <string>

using namespace std;

int main(){
    int times;
    cin >> times;
    for (int i = 0; i < times;i++){
        string temp;
        cin >> temp;
        if(temp.length()>10){
            cout << temp.at(0);
            cout << temp.length() - 2;
            cout << temp.at(temp.length()-1) << "\n";
        }else
        {
            cout << temp << "\n";
        }
    }
}