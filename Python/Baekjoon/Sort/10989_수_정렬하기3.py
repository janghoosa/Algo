# 10989 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
import sys

N = int(sys.stdin.readline())
A = [0 for _ in range(10001)]
for _ in range(N):
    tmp = int(sys.stdin.readline())
    A[tmp] += 1
for i in range(10001):
    for j in range(A[i]):
        print(i)