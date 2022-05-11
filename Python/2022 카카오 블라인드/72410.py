# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
# 신규 아이디 추천
import re
def solution(new_id):
    answer = ''
    answer = re.sub('[^a-z\d\-\_\.]','',new_id.lower())
    answer = re.sub('\.\.+','.',answer)
    answer = re.sub('^\.|\.$', '', answer)
    answer = re.sub('^\.|\.$', '', answer)
    if answer == '':
        answer = 'a'
    answer = re.sub('\.$', '', answer[0:15])
    while len(answer) < 3:
        answer += answer[-1:]
    return answer