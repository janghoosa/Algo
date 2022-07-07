# 18870 좌표 압축
# https://www.acmicpc.net/problem/18870
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = sorted(set(A))
C = {}
for i in range(len(B)):
    C[B[i]] = i
for j in A:
    print(C[j], end=' ')