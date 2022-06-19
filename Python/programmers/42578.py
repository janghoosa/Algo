# 해시
# 프로그래머스 42578 위장 
# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    dic = dict()
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    print(dic)        
    
    for i in dic:
        answer *= (dic[i]+1)
    return answer-1