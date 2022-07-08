# 14425 문자열
# https://www.acmicpc.net/problem/14425
N, M = map(int, input().split())
A ={}
for i in range(N):
    tmp = input()
    A[tmp] = 1
B = [input() for _ in range(M)]
ans = 0
for i in B:
    if i in A:
        ans += 1

print(ans)