# 15386 퇴사 2
# https://www.acmicpc.net/problem/15486
import sys 
input = sys.stdin.readline 

N = int(input())
counsel = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    end = i + counsel[i-1][0] -1
    if end <= N:
        dp[end] = max(dp[end], dp[i-1]+counsel[i-1][1])

print(max(dp))