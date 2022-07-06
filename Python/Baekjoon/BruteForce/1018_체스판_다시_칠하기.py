# 1018 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]

def check88(x, y):
    res = 0
    res2 = 0
    for i in range(8):
        for j in range(8):
            tmp = A[y+j][x+i]
            if (i+j)%2 == 0:
                if tmp != 'W':
                    res += 1
                if tmp != 'B':
                    res2 += 1
            else:
                if tmp != 'B':
                    res += 1
                if tmp != 'W':
                    res2 += 1
    return min(res, res2)

ans = 10000
for i in range(N-7):
    for j in range(M-7):
        # print(i, j)
        ans = min(ans,check88(j, i))
print(ans)