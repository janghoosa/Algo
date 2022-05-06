# https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3
# 거리두기 확인하기

D = ((-1,0),(1,0),(0,-1),(0,1))
D2 = ((-1,-1),(-1,1),(1,-1),(1,1))

def check(room):
    for i in range(5):
        for j in range(5):
            if room[i][j] != 'P':
                continue
            for d in range(4):
                x, y = i+D[d][0], j+D[d][1]
                
                if x < 0 or x > 4 or y < 0 or y > 4:
                    continue
                elif room[x][y] == 'P':
                    return 0
            
            for d in range(4):
                x, y = i+D2[d][0], j+D2[d][1]
                if x < 0 or x > 4 or y < 0 or y > 4:
                    continue
                elif room[x][y] == 'P':
                    if(room[i][y] != 'X' or room[x][j]!='X'):
                        return 0
            
            for d in range(4):
                x, y = i+2*D[d][0], j+2*D[d][1]
                dx, dy = i+D[d][0], j+D[d][1]
                if x < 0 or x > 4 or y < 0 or y > 4:
                    continue
                elif room[x][y] == 'P':
                    if room[dx][y] != 'X' and room[x][dy] !='X':
                        return 0
    return 1
          
    
def solution(places):
    answer = []
    for room in places:
        if check(room):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer