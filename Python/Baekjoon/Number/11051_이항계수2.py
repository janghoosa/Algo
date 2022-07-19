# 11051 이항계수 2
# https://www.acmicpc.net/problem/11051
import math
N, M = map(int,input().split())
A=[]

for i in range(N+1) :
    A.append([1]*(i+1))

for i in range(2, N+1) :
    for j in range(1, i) :
        A[i][j]=(A[i-1][j-1]+A[i-1][j])%10007

print(A[N][M])