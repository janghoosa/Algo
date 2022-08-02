# 21610 마법사 상어와 비바라기
# https://www.acmicpc.net/problem/21610
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

C = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]

def moveC(di,si):
    for i in range(len(C)):
        tmpy = C[i][0]+(dy[di]*si)
        tmpx = C[i][1]+(dx[di]*si)

        while tmpx < 0:
            tmpx += N
        while tmpx >= N:
            tmpx -= N
        while tmpy < 0:
            tmpy += N
        while tmpy >= N:
            tmpy -= N
        C[i][0] = tmpy
        C[i][1] = tmpx

def wCopy(y,x):
    dx2 = [-1, 1, 1, -1]
    dy2 = [-1, -1, 1, 1]
    for i in range(4):
        if 0 <= dy2[i] + y < N and 0 <= dx2[i] + x < N:
            if A[dy2[i] + y][dx2[i] + x] > 0:
                A[y][x] += 1

for i in B:
    moveC(i[0]-1, i[1])
    wCopyList = []
    visit = [[False]*N for _ in range(N)]
    for j in C:
        A[j[0]][j[1]] += 1
        wCopyList.append([j[0],j[1]])
        visit[j[0]][j[1]] = True
    for j in wCopyList:
        wCopy(j[0], j[1])
    C2 = []
    for j in range(N):
        for k in range(N):
            if A[j][k] >= 2 and visit[j][k] == False:
                A[j][k] -= 2
                C2.append([j,k])
    C = C2

ans = 0
for i in range(N):
    for j in range(N):
        ans += A[i][j]
print(ans)

# 5 1
# 0 0 1 0 2
# 2 3 2 1 0
# 4 3 2 9 0
# 1 0 2 9 0
# 8 8 2 1 0
# 1 3