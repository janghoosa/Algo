# https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3
# 신고 결과 받기
def solution(id_list, report, k):
    answer = []
    table = {}
    table2 = {}
    for i in id_list:
        table[i] = ([],[0])
        table2[i] = []
    for rep in report:
        report = rep.split()[0]
        criminal = rep.split()[1]
        if report not in table[criminal][0]:
            table[criminal][0].append(report)
            table[criminal][1][0] += 1
            table2[report].append(criminal)
    fire = []
    for i in id_list:
        if table[i][1][0] >= k:
            fire.append(i)
    for i in id_list:
        count = 0
        for f in fire:   
            if f in table2[i]:
                count += 1
        answer.append(count)
    return answer