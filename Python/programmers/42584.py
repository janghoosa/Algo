# 큐
# 프로그래머스 42584 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584
# from collections import deque
def solution(prices):
    answer = []
    dq = deque(prices)
    while dq:
        tmp = dq.popleft()
        cost = 0
        for i in dq:
            cost += 1
            if i < tmp:
                break
        answer.append(cost)
    return answer