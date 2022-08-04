# 21600 계단
# https://www.acmicpc.net/problem/21600
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
dp = list(0 for _ in range(N+1))
dp[1] = A[1]
for i in range(1,N+1):
    if A[i]>A[i-1]:
        dp[i] = dp[i-1]+1
    elif A[i] == A[i-1]:
        dp[i] = dp[i-1]
    else:
        if dp[i-1] < A[i]:
            dp[i] = dp[i-1]+1
        elif dp[i-1] == A[i]:
            dp[i] = dp[i-1]
        else:
            dp[i] = A[i]
print(max(dp))