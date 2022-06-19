# 큐
# 프로그래머스 42587 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque
def solution(priorities, location):
    answer = 0
    
    dq = deque(priorities)
    
    while True:
        tmp = dq.popleft()
        location -= 1
        flag = False
        for i in dq:
            if(i > tmp):
                flag = True
                break
            else:
                flag = False
        if flag:
            dq.append(tmp)
            if location == -1:
                location += len(dq)
        else:
            answer += 1
            if location == -1:
                break

    return answer