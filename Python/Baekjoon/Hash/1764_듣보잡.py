# 1764 듣보잡
# https://www.acmicpc.net/problem/1764
N, M = map(int, input().split())
A = {}
for _ in range(N):
    tmp = input()
    A[tmp] = 1
B = [input() for _ in range(M)]
ans = 0
C = []
for i in B:
    if i in A:
        ans += 1
        C.append(i)
print(ans)
C.sort()
for i in C:
    print(i)
