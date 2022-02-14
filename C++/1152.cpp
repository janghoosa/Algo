#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    answer.push_back(numbers[0] + numbers[1]);
    for (int i = 0; i < numbers.size() - 1; i++) {
        for(int j = i + 1; j < numbers.size(); j++){
            for(int k = 0; k < answer.size();k++){
                if(numbers[i]+numbers[j] == answer[k]){
                    break;
                }
                if(answer[k] > numbers[i]+numbers[j]){
                    answer.insert(answer.begin() + k, numbers[i] + numbers[j]);
                    break;
                }
                if((k + 1) >= answer.size()){
                    answer.push_back(numbers[i]+numbers[j]);
                }
            }
        }
    }

    return answer;
}