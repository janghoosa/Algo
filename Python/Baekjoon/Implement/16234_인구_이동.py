# 16234 인구 이동
# https://www.acmicpc.net/problem/16234
import sys

input = sys.stdin.readline
from collections import deque
N, L, R = map(int, input().split())
A = [list(0 for _ in range(N)) for _ in range(N)]
for y in range(N):
    tmp = list(map(int,input().split()))
    for x in range(N):
        A[y][x] = tmp[x]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(y, x):
    visited[y][x] = 1
    visit = []
    queue = deque([[y,x]])
    while queue:
        ty, tx = queue.popleft()
        visit.append([ty,tx])
        
        for i in dir:
            if 0<=ty+i[0]<N and 0<=tx+i[1]<N and visited[ty+i[0]][tx+i[1]] == 0:
                if L<=abs(A[ty+i[0]][tx+i[1]]-A[ty][tx])<=R:
                    queue.append([ty+i[0], tx+i[1]])
                    visited[ty+i[0]][tx+i[1]] = 1
    return visit
ans = 0
while True:
    visited = [list(0 for _ in range(N)) for _ in range(N)]
    country = []
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:
                country.append(bfs(y,x))
    flag = True
    for nation in country:
        if len(nation) == 1:
            continue
        flag = False
        population = sum([A[y][x] for y, x in nation]) // len(nation)
        for y, x in nation:
            A[y][x] = population
    if flag:
        break
    ans += 1
print(ans)