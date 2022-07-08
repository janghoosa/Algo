# 10815 숫자 카드
# https://www.acmicpc.net/problem/10815
N = int(input())
A = {}
tmp = input().split()
for i in range(N):
    A[int(tmp[i])] = 1
M = int(input())
B = list(map(int,input().split()))
for i in B:
    if i in A:
        print(1, end=' ')
    else:
        print(0, end=' ')