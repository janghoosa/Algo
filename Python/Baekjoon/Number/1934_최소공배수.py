# 1934 최소공배수
# https://www.acmicpc.net/problem/1934
N = int(input())
def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)
for _ in range(N):
    A, B = map(int, input().split())
    GCD = gcd(A,B)
    print(int(A*B/GCD))