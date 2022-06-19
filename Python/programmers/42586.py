# 스택
# 프로그래머스 42586 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

import math
def solution(progresses, speeds):
    answer = []
    day =[]
    for i in range(len(progresses)):
        day.append(math.ceil((100-progresses[i])/speeds[i])) 
    index = -1
    maxDay = 0
    for i in day:
        if maxDay < i:
            maxDay = i
            answer.append(1)
            index += 1
        else:
            answer[index] += 1
    return answer