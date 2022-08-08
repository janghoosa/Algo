# 11559 Puyo Puyo
# https://www.acmicpc.net/problem/11559
from collections import deque
A = [list(input()) for _ in range(12)]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs(y,x):
    visited[y][x] = True
    dq = deque()
    dq.append((y,x))

    pang = deque()
    pang.append((y,x))

    cnt = 1
    while dq:
        my, mx = dq.popleft()
        for i in range(4):
            tx = mx + dx[i]
            ty = my + dy[i]
            if 0 <= ty < 12 and 0 <= tx < 6:
                if A[y][x] == A[ty][tx] and visited[ty][tx] == False:
                    dq.append((ty,tx))
                    pang.append((ty,tx))
                    visited[ty][tx] = True
                    cnt += 1
    if cnt >= 4:
        for y,x in pang:
            A[y][x] = '.'
        return 1
    return 0

def drop():
    dq = deque()
    for x in range(6):
        for y in range(11,-1,-1):
            if A[y][x] != '.':
                dq.append(A[y][x])
        for y in range(11,-1,-1):
            if dq:
                A[y][x] = dq.popleft()
            else:
                A[y][x] = '.'


res = 0
while True:
    visited = [[False]*6 for _ in range(12)]
    ans = 0
    for x in range(6):
        for y in range(12):
            if A[y][x] != '.' and visited[y][x] == 0:
                ans += bfs(y,x)
    if ans == 0:
        print(res)
        break
    else:
        res += 1
    drop()