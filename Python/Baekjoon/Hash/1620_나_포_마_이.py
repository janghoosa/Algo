# 1620 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = {}
for i in range(1, N+1):
    tmp = input().rstrip()
    A[tmp] = i
    A[i] = tmp
B = [input().rstrip() for _ in range(M)]
for i in B:
    if i.isnumeric():
        print(A[int(i)])
    else:
        print(A[i])