# 2231 분해합
# https://www.acmicpc.net/problem/2231
N = int(input())
ans = 0
for i in range(N):
    tmp = sum(map(int,str(i)))
    Sum = i + tmp
    if N == Sum:
        ans = i
        break
print(ans)