# 1676 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676
import math
N = int(input())

def findNum(num, k):
    cnt = 0
    while num:
        num//=k
        cnt += num
    return cnt

n2 = findNum(N, 2)
n5 = findNum(N, 5)
print(min(n2, n5))