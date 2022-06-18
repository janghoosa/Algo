# 해쉬
# 프로그래머스 42577 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
def solution(phone_book):
    answer = True
    dic = {}
    for i in phone_book:
        dic[i] = 1
        
    for i in phone_book:
        tmp = ""
        for num in i:
            tmp += num
            if tmp in dic and tmp !=i:
                answer = False
    return answer