# 1036 약수
# https://www.acmicpc.net/problem/1037
N = int(input())
A = list(map(int, input().split()))
Min = 1000001
Max = 0
for tmp in A:
    Min = min(Min, tmp)
    Max = max(Max, tmp)
print(Min * Max)
