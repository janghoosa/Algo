# 1269 대칭 차집합
# https://www.acmicpc.net/problem/1269
N, M = map(int, input().split())
A = {}
B = {}
tmp = input().split()
for i in range(N):
    A[int(tmp[i])] = 1
tmp = input().split()
for i in range(M):
    B[int(tmp[i])] = 1
ans = 0
for i in A:
    if i not in B:
        ans += 1
for i in B:
    if i not in A:
        ans += 1
print(ans)