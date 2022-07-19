# 9375 패션왕 신해빈
# https://www.acmicpc.net/problem/9375
N = int(input())
for _ in range(N):
    M = int(input())
    A = {}
    for _ in range(M):
        i1, i2 = input().split()
        if i2 in A:
            A[i2] += 1
        else:
            A[i2] = 1
    if len(A.keys()) == 1:
        for i in A:
            print(A[i])
    else:
        ans = 1
        for i in A:
            ans *= A[i]+1
        print(ans-1)