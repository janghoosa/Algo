# 3036 링
# https://www.acmicpc.net/problem/3036
from fractions import Fraction
N = int(input())
A = list(map(int, input().split()))
for i in range(1,N):
    tmp = Fraction(A[0],A[i])
    print(str(tmp.numerator)+'/'+str(tmp.denominator))