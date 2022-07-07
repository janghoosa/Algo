# 2751 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
import sys

N = int(sys.stdin.readline())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A.sort()
for i in A:
    print(i)