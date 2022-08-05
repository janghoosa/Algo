# 2096 내려가기
# https://www.acmicpc.net/problem/2096
import sys
input = sys.stdin.readline
N = int(input())

dpmin = [[0 for _ in range(3)] for _ in range(2)]
dpmax = [[0 for _ in range(3)] for _ in range(2)]
for i in range(N):
    tmp = list(map(int, input().split()))
    dpmax[1][0] = max(dpmax[0][0], dpmax[0][1])+ tmp[0]
    dpmin[1][0] = min(dpmin[0][0], dpmin[0][1])+ tmp[0]

    dpmax[1][1] = max(dpmax[0][0], dpmax[0][1], dpmax[0][2])+ tmp[1]
    dpmin[1][1] = min(dpmin[0][0], dpmin[0][1], dpmin[0][2])+ tmp[1]

    dpmax[1][2] = max(dpmax[0][1], dpmax[0][2])+ tmp[2]
    dpmin[1][2] = min(dpmin[0][1], dpmin[0][2])+ tmp[2]
    
    for i in range(3):
        dpmax[0][i] = dpmax[1][i]
        dpmin[0][i] = dpmin[1][i]

print(max(dpmax[1]),min(dpmin[1]))