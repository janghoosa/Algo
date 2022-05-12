# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
# 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    stack = [0]
    for ins in moves:
        selected = 0
        for lines in board:
            if lines[ins-1] != 0:
                selected = lines[ins-1]
                lines[ins-1] = 0
                pop = stack[-1]
                if pop == selected:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(selected)
                break
                
    return answer