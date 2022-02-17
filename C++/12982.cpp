#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    int tempBudget = 0;
    sort(d.begin(),d.end());
    for(int i=0 ; i < d.size(); i++){
        if((tempBudget + d[i])>budget){
            continue;
        }else {
            tempBudget += d[i];
            answer += 1;
        }
    }
    return answer;
}