# 정렬
# 프로그래머스 42747 H-index
# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            answer = len(citations)-i
            break
    return answer