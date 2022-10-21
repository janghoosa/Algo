# 113501 야간 전술보행
# https://school.programmers.co.kr/learn/courses/30/lessons/133501
def solution(distance, scope, times):
    answer = 0
    pos = 0
    
    def checkS(time, now):
        work, rest = time
        if now > work + rest:
            temp = now % (work+rest)
            return False if temp == 0 or temp > work else True
        else:
            return False if now > work else True
        
        
    security = [[] for _ in range(distance)]
    for idx, data  in enumerate(scope):
        start, end = data
        if start > end:
            start, end = end, start
        for i in range(start, end+1):
            security[i].append(idx)
    while pos < distance:
        if security[pos]:
            for chk in security[pos]:
                if checkS(times[chk], pos):
                    answer = pos
                    return answer
        pos += 1
        answer = pos
    return answer