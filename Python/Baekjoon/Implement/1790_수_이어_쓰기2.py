# 1790 수 이어 쓰기 2
# https://www.acmicpc.net/problem/1790
N, K = map(int, input().split())
ans = True
for i in range(1, N+1):
    data = str(i)
    if len(data) >= K:
        ans = False
        print(data[K-1])
        break
    K -= len(data)
if ans :
    print(-1)