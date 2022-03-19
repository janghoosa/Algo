#include <iostream>

using namespace std;

int main(){
    int in, count = 0;
    int in1 = 0, in2 = 0, in3 = 0, in4 = 0;

    cin >> in;

    for (int i = 0; i < in;i++){
        int input;
        cin >> input;
        if (input == 1) in1++;
        else if( input == 2) in2++;
        else if( input ==3 ) in3++;
        else in4++;
    }
    count += in4;
    count += in3;
    if(in1 < in3){
        in1 -= in1;
    } else {
        in1 -= in3;
    }
    count += (in2 / 2);
    in2 -= (in2 / 2) * 2;
    if(in2 ==1){
        count++;
        if(in1 > 2){
            in1 -= 2;
        } else{
            in1 -= in1;
        }
    }
    count += in1 / 4;
    in1 = in1 % 4;
    if (in1 > 0) {
        count++;
    }
    cout << count << '\n';

    return 0;
}