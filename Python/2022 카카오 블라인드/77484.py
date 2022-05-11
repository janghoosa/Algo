# https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3
# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = []
    wild = 0
    pos = 0
    for i in lottos:
        if i == 0:
            wild += 1
        else:
            if i in win_nums:
                pos += 1
    
    score = pos+wild
    if score == 0:
        answer.append(6)
    else:
        answer.append(7-score)
    
    score = pos
    if score == 0:
        answer.append(6)
    else:
        answer.append(7-score)
    
    return answer