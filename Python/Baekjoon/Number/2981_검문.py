# 2981 검문
# https://www.acmicpc.net/problem/2981
import math
N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()
interval = [A[i] - A[i-1] for i in range(1, N)]

GCD = interval[0]
for i in range(1, N-1):
    GCD = math.gcd(GCD,interval[i])

ans = []
for i in range(1, int(math.sqrt(GCD))+1):
    if GCD % i ==0:
        if pow(i, 2) == GCD:
            ans.append(i)
        else:
            ans += [i, GCD // i]
ans.remove(1)
ans.sort()
print(*ans)