# 2750 수 정렬하기
# https://www.acmicpc.net/problem/2750
N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()
for i in A:
    print(i)