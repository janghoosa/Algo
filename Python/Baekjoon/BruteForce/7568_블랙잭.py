# 2798 블랙잭
# https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())
card = list(map(int,input().split()))
Max = 0
for i in range(0, len(card)-2):
    for j in range(i+1 ,len(card)-1):
        for k in range(j+1 ,len(card)):
            tmp = card[i]+card[j]+card[k]
            if tmp <= M:
                Max = max(tmp, Max)
print(Max)