#include <string>
#include <vector>

using namespace std;

int solution(vector<int> absolutes, vector<bool> signs) {
    int answer = 0;
    for(int i =0;i<absolutes.size();i++){
        if(signs.at(i)){
            answer += absolutes.at(i);
        }else {
            answer -= absolutes.at(i);
        }
    }
    return answer;
}