# 11650 좌표 정렬하기
# https://www.acmicpc.net/problem/11650
import sys
N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
A.sort()
for i in A:
    print(i[0],i[1])