# 10827 a^b
# https://www.acmicpc.net/problem/10827
from decimal import Decimal, getcontext
A = input().split()
a = A[0]
b = int(A[1])
getcontext().prec = 2000
print("{0:f}".format(Decimal(a)**b))