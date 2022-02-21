// https://programmers.co.kr/learn/courses/30/lessons/1845
#include <vector>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    bool ischecked[200001]={false,};
    for(int i=0;i<nums.size();i++){
        if(!ischecked[nums.at(i)]){
            answer += 1;
            ischecked[nums.at(i)]= true;
        }
    }
    if(nums.size()/2 < answer){
        answer = nums.size()/2;
    }
    return answer;
}