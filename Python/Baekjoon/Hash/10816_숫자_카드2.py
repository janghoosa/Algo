# 10816 숫자 카드 2
# https://www.acmicpc.net/problem/10816
N = int(input())
A = {}
tmp = input().split()
for i in range(N):
    if int(tmp[i]) in A:
        A[int(tmp[i])] += 1
    else:
        A[int(tmp[i])] = 1
M = int(input())
B = list(map(int,input().split()))
for i in B:
    if i in A:
        print(A[i], end=' ')
    else:
        print(0, end=' ')