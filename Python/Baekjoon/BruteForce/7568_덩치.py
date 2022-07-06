# 7568 덩치
# https://www.acmicpc.net/problem/7568
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

for i in A:
    ans = 1
    for j in A:
        if i[0] < j[0] and i[1] < j[1]:
            ans += 1
    print(ans, end=" ")