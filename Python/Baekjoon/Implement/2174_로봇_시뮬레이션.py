# 2174 로봇 시뮬레이션
# https://www.acmicpc.net/problem/2174
A, B = map(int, input().split())
N, M = map(int, input().split())
visited = [[0 for _ in range(A)] for _ in range(B)]
Robot = []
for _ in range(N):
    tmp = input().split()
    Robot.append([int(tmp[1])-1,int(tmp[0])-1,tmp[2]])
actions = []
for _ in range(M):
    tmp = input().split()
    actions.append([int(tmp[0])-1,tmp[1],int(tmp[2])])

for i in range(N):
    visited[Robot[i][0]][Robot[i][1]] = i+1
ans = True
for action in actions:
    if action[1] == 'F':
        # moveFoward()
        direction = Robot[action[0]][2]
        x = int(Robot[action[0]][1])
        y = int(Robot[action[0]][0])
        dx = dy = 0
        if direction == 'N':
            dy = +1
        elif direction == 'S':
            dy = -1
        elif direction == 'W':
            dx = -1
        elif direction == 'E':
            dx = 1
        for i in range(1,int(action[2])+1):
            if x + dx * i < 0 or x + dx * i >= A or y + dy*i < 0 or y + dy*i >= B:
                # print(x + dx < 0 ,x + dx , A ,y + dy < 0 , y + dy >= B)
                # print(x,dx,y,dy)
                # print(action)
                # print(Robot)
                # print(visited)
                print("Robot "+str(action[0]+1)+" crashes into the wall")
                ans = False
                break
            if visited[y+dy*i][x+dx*i] > 0:
                # print(action)
                # print(Robot)
                # print(visited)
                print("Robot "+str(action[0]+1)+" crashes into robot "+str(visited[y+dy*i][x+dx*i]))
                ans = False
                break
        if ans == False:
            break
        Robot[action[0]][1] = x+dx*int(action[2])
        Robot[action[0]][0] = y+dy*int(action[2])
        visited[y][x] = 0
        visited[y+dy*int(action[2])][x+dx*int(action[2])] = action[0]+1
    elif action[1] == 'L':
        # turnLeft()
        direction = Robot[action[0]][2]
        for i in range(action[2]%4):
            if direction == 'N':
                direction = 'W'
            elif direction == 'S':
                direction = 'E'
            elif direction == 'W':
                direction = 'S'
            elif direction == 'E':
                direction = 'N'
            Robot[action[0]][2] = direction
    elif action[1] == 'R':
        # turnRight()
        direction = Robot[action[0]][2]
        for i in range(action[2]%4):
            if direction == 'N':
                direction = 'E'
            elif direction == 'S':
                direction = 'W'
            elif direction == 'W':
                direction = 'N'
            elif direction == 'E':
                direction = 'S'
        Robot[action[0]][2] = direction
    
if ans:
    print("OK")