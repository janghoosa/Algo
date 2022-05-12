# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
# 키패드 누르기
def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    bleft = 10
    bright = 12
    for i in numbers:
        if i == 0:
            i = 11
        if i in left:
            answer += 'L'
            bleft = i
        elif i in right:
            answer += 'R'
            bright = i
        else:
            if bright - i > 0:
                r = bright-i
            else:
                r = i -bright
            if bleft -i > 0:
                l = bleft-i
            else:
                l = i - bleft
            R = r%3 + r//3
            L = l%3 + l//3
            if R == L:
                if hand == 'right':
                    answer+='R'
                    bright = i
                else:
                    answer+='L'
                    bleft = i
            elif R < L:
                answer+='R'
                bright = i
            else:
                answer+='L'
                bleft = i
    return answer