# 9011 순서
# https://www.acmicpc.net/problem/9011
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    flag = False
    ans = [0 for _ in range(n)]
    ans[-1] = A[-1]+1
    used = [A[-1]+1]
    for i in range(n-2, -1, -1):
        res = A[i]+1
        used.sort()
        for j in used:
            if res >= j:
                res += 1
        if res > n:
            flag = True
            break
        ans[i] = res
        used.append(res)
    if flag:
        print('IMPOSSIBLE')
    else:
        print(*ans)