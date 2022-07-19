# 1010 다리 놓기
# https://www.acmicpc.net/problem/1010
import math
N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    print(math.factorial(B)//(math.factorial(A)*math.factorial(B-A)))
