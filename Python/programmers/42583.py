# 큐
# 프로그래머스 42583 다리는 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    cost = 0
    dq = deque(truck_weights)
    dq2 = deque([0 for _ in range(bridge_length)])
    while len(dq) > 0 or cost > 0:
        tmp = dq2.popleft()
        cost -= tmp
        
        if len(dq) and cost + dq[0] <= weight:
            tmp2 = dq.popleft()
            dq2.append(tmp2)
            cost += tmp2
        else:
            dq2.append(0)
            
        answer += 1
        
    return answer