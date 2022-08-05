# 21600 계단
# https://www.acmicpc.net/problem/21600
N = int(input())
A = list(map(int, input().split()))
stair = 0
ans = 0
for i in A:
    if stair+1 <= i:
        stair = stair+1 
    else:
        stair = i
    print(stair)
    ans = max(ans, stair)
print(ans)