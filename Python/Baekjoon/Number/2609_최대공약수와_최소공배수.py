# 2609 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609
def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

N, M = map(int,input().split())
d = gcd(N, M)
m = int((N*M)/d)
print(d)
print(m)