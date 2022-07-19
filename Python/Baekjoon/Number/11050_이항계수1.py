# 11050 이항계수 1
# https://www.acmicpc.net/problem/11050
import math
N, M = map(int,input().split()) 
ans = math.factorial(N)/math.factorial(M)/math.factorial(N-M)
print(int(ans)%10007)