# 2004 조합 0의 개수
# https://www.acmicpc.net/problem/2004

def findNum(num, k):
    cnt = 0
    while num:
        num//=k
        cnt += num
    return cnt

N, M = map(int, input().split())
N2 = findNum(N, 2) - findNum(M, 2) - findNum(N-M, 2)
N5 = findNum(N, 5) - findNum(M, 5) - findNum(N-M, 5)
print(min(N2, N5))