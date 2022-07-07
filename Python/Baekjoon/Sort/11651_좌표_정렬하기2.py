# 11651 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651
import sys
from operator import itemgetter
N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
A = sorted(A,key=lambda x: (x[1],x[0]))
for i in A:
    print(i[0],i[1])