# 2108 통계학
# https://www.acmicpc.net/problem/2108
import sys
from collections import Counter

N = int(sys.stdin.readline())
A = []
cnt = 0
for _ in range(N):
    tmp = int(sys.stdin.readline())
    A.append(tmp)
    cnt += tmp
A.sort()
mode = Counter(A)
mode2 = mode.most_common(2)
print(round(cnt/N))
print(A[N//2])
if N != 1:
    if mode2[0][1] == mode2[1][1]:
        print(mode2[1][0])
    else:
        print(mode2[0][0])
else:
    print(A[0])
print(A[N-1]-A[0])