#include <string>
#include <vector>
#include <math.h>

using namespace std;

int factor(int n){
    int count = 0;
    for(int i=1;i<=sqrt(n);i++){
        if(n % i == 0){
            if(n/i==i){
                count += 1;
            }
            else {
                count += 2;
            }
        }        
    }
    return count;
}

int solution(int left, int right) {
    int answer = 0;
    for(int i=left;i<=right;i++){
        if(!((factor(i)) % 2 == 1)){
            answer += i;
        }
        else {
            answer -= i;
        }
    }
    return answer;
}